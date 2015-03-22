# -*- coding: utf-8 -*-
# 
# Created on 08 Nov 2011
# @author: PL Young
#=======================================================================================================================

import logging
import urllib
import webapp2
import traceback
from google.appengine.api import taskqueue, urlfetch
from webapp2_extras.auth import security
from game.models import PaypalTransaction

class paypal_task_processor1(webapp2.RequestHandler):
    # 1st step, save the paypal request to db and start 2nd step
    def post(self):
        # only interrested in Completed transactions
        payment_status = self.request.get('payment_status', '')
        if payment_status != 'Completed':
            return
    
        # check if this transaction has not already been saved
        transaction_id = self.request.get('txn_id', '')
        q = PaypalTransaction.query(PaypalTransaction.transaction_id == transaction_id) 
        pp = q.get()
        if pp:
            return # found in db, dont make duplicate

        # -----------------------------------------------------------------        
        # save the transaction request 
        orig_query = ''                                         # need to send this back to paypal later
        for k, v in self.request.str_POST.iteritems():
            orig_query += '&' + k + '=' + v
        
        item_name = self.request.get('item_name', '')           # what was purchased
        payment_gross = self.request.get('mc_gross', '')        # how much was payed, should check and flag if not valid
        
        player_email = self.request.get('option_selection1', '')# the account for which game should be unlocked (or a key be send to)
        customer_email = self.request.get('payer_email', '')    # just incase player_email fails
        customer_name = self.request.get('first_name', '') + ' ' + self.request.get('last_name', '')

        pp = PaypalTransaction()
        pp.transaction_status = 0 # 0=this still needs to be validated
        pp.orig_query = orig_query
        pp.transaction_id = transaction_id
        pp.item_name = item_name
        pp.payment_gross = payment_gross
        pp.player_email = player_email
        pp.customer_email = customer_email
        pp.customer_name = customer_name
        pp.gamekey_used = '' # not yet used (account/login email will be here when used)
        pp.gamekey = ''
        
        try:
            pp.put()
            taskqueue.add(queue_name='default', url='/work/pay_pp2/', params=self.request.str_POST)
        except:
            logging.error("Failed to write new PaypalTransaction for: " + customer_email)
            taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={
                        'email':'YOUR_EMAIL',
                        'subject':'GAME_NAME_HERE: PaypalTransaction failed',
                        'body':'Check transaction for: ' + str(customer_email) + " ("+str(transaction_id)+")",
                        })
    
class paypal_task_processor2(webapp2.RequestHandler):
    # 2nd step, ask paypal if it was a valid request
    def post(self):
        
        test_ipn = self.request.get('test_ipn', '0')
        customer_email = self.request.get('payer_email', '')
        transaction_id = self.request.get('txn_id', '')
        
        url = "https://www.paypal.com/cgi-bin/webscr?"
        if test_ipn=='1':
            url = "https://www.sandbox.paypal.com/cgi-bin/webscr?"
        
        req = 'cmd=_notify-validate';
        for k, v in self.request.str_POST.iteritems():
            req += '&' + k + '=' + v        

        req = urllib.quote(req)

        try:
            #res = urlfetch.fetch(url, payload=req, method=urlfetch.POST, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            res = urlfetch.fetch(url+req, method=urlfetch.GET)
            
            # Verify that the response status is 200
            # response will be either VERIFIED or INVALID
            if res.status_code != 200:
                taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={
                        'email':'YOUR_EMAIL',
                        'subject':'GAME_NAME_HERE: PaypalTransaction failed',
                        'body':'status_code!=200; Check transaction for: ' + str(customer_email) + " ("+str(transaction_id)+")",
                        })
                return
    
            if res.content == 'INVALID':
                taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={
                        'email':'YOUR_EMAIL',
                        'subject':'GAME_NAME_HERE: PaypalTransaction failed',
                        'body':'PayPal said INVALID; Check transaction for: ' + str(customer_email) + " ("+str(transaction_id)+")",
                        })
                return
                
            # update db and send buyer the code
            q = PaypalTransaction.query(PaypalTransaction.transaction_id == transaction_id) 
            pp = q.get()
            if pp:
                pp.transaction_status = 1
                # generate a game unlock key (at least 12 characters long)
                pp.gamekey = str(pp.key.id())
                l = 12 - len(pp.gamekey)
                if l > 0: 
                    pp.gamekey += security.generate_random_string(l).upper()
                pp.put()
    
                # send email (send to person who payed too if player and customer emails differ)
                game_name = webapp2.get_app().config['APP_INFO']['NAME']
                game_url = webapp2.get_app().config['APP_INFO']['URL']
                email1 = pp.player_email
                email2 = pp.customer_email
                if email1:
                    if len(email1)>0:
                        if email2:
                            if email1.lower() == email2.lower():
                                email2 = None 
                subject = game_name + " Purchase"
                body = """
Thankyou for purchasing %s

Your gamekey is: %s

Please use this key to unlock the selected game features by going to your profile section in the game.
For more information, visit %s

Thank you
""" % (game_name, pp.gamekey, game_url)
                    
                if email1:    
                    if len(email1)>0:
                        taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={'email':email1,'subject':subject,'body':body})
                if email2:    
                    if len(email2)>0:
                        taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={'email':email2,'subject':subject,'body':body})

            else:
                logging.error("Failed to verify PaypalTransaction: " + str(customer_email) + "\n PP was not valid")
                taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={
                            'email':'YOUR_EMAIL',
                            'subject':'GAME_NAME_HERE: PaypalTransaction failed',
                            'body':'[EXCEPTION] Check transaction for: '+customer_email+' ('+transaction_id+')'
                            })

        except:
            logging.error("Failed to verify PaypalTransaction: " + str(customer_email) + "\n"+ str(traceback.format_exc()))
            taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={
                        'email':'YOUR_EMAIL',
                        'subject':'GAME_NAME_HERE: PaypalTransaction failed',
                        'body':'[EXCEPTION] Check transaction for: '+customer_email+' ('+transaction_id+')'
                        })
    
class paypal(webapp2.RequestHandler):
    def post(self):
        # PayPal will send a request containing various variables

        # do not want to process requests from sandbox
        # comment this out while testing with paypal sandbox
        test_ipn = self.request.get('test_ipn', '0')
        if test_ipn=='1':
            return

        # verify receiver e-mail
        receiver_email = self.request.get('receiver_email', '0')
        if receiver_email!="YOUR_PAYPAL_EMAIL_HERE":
            return
        
        # dump it into the task queue
        taskqueue.add(queue_name='default', url='/work/pay_pp1/', params=self.request.str_POST)
        
#=======================================================================================================================
