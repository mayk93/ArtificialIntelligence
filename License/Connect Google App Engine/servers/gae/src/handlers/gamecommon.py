# -*- coding: utf-8 -*-
# 
# Created on 03 Aug 2011
# @author: PL Young
#=======================================================================================================================

import logging
import time
import random
import webapp2
from google.appengine.api import mail, taskqueue
from webapp2_extras import auth 
from webapp2_extras.auth import security
import game
from game.models import User, UserToken, Advert, PaypalTransaction, News

#---------------------------------------------------------------------------------------------------------------------- 

class account(game.GameRequestHandler):
    
    def login(self):
        """ Login erquested from within game client """
        nm = self.get_post('nm', '!').lower()
        pw = self.get_post('pw', '!')
        self.out = '0'
        self.a_user = None
        try:                
            a = auth.get_auth() 
            self.a_user = a.get_user_by_password("own:" + nm, pw, remember=True, save_session=True)
        except auth.InvalidAuthIdError:
            self.out = '0Invalid E-mail'
        except auth.InvalidPasswordError:
            self.out = '0Invalid Password'
        
        # user found and password checked out
        if self.a_user:
            self.out = '0Server error. Please try again in a few minutes.'
            
            self.user_token = UserToken.get(user=self.a_user['user_id'], subject='auth', token=self.a_user['token'])
            if not self.user_token:
                self.out = '0Server error 1. Please try again in a few minutes.'

            self.user = User.get_by_id(self.a_user['user_id'])
            if not self.user:
                self.out = '0Server error 2. Please try again in a few minutes.'
                
            if self.user and self.user_token:
                uid = int(self.user.get_id())

                # update the token
                now = int(time.time())
                self.user_token.uid = uid
                self.user_token.plrname = self.user.name
                self.user_token.location = 'L' # in lobby
                self.user_token.last_game_refresh = now
                self.user_token.last_chat_refresh = now
                self.user_token.put();
                
                self.out = '1'
                
                # send the auth cookie in the body too just incase i cant read it from header                
                self.out += 'auth='+self.session_store.serializer.serialize('auth', a.session)                
                          
                # output player name      
                self.out += '^' + self.user.name + '^'
                                
                # tell client which parts of game the player own
                #for s in self.user.shop.values():
                #    self.out += s
                self.out += ''.join(self.user.shop) + '^'

                # send settings
                self.out += '1^' if self.user.email_bmchallenge else '0^'                

        self.respond()
                
    def changepw(self):
        if not self.auth():
            self.respond('!'); return # not authenticated
        
        old_pw = self.get_post('a', '')
        password = self.get_post('b', '')
        
        if len(old_pw)<1:
            self.respond("0You did not provide your old password."); return
            
        if len(password)<5 or len(password)>15:
            self.respond("0Please enter a new password of between 5 and 15 characters."); return
        
        if not security.check_password_hash(old_pw, self.user.password):
            self.respond("0Your old password was invalid"); return
        
        self.user.password = security.generate_password_hash(password, length=12)
        try:
            self.user.put()
        except:
            self.respond("0Could not update your password. Please try again later.")
            return                
        
        self.respond('1')
    
    def recoverpw(self):
        email = self.get_post('em', '')
        
        if not mail.is_email_valid(email):
            self.respond("0Please enter a valid e-mail address."); return
        
        # find the user from e-mail
        email = email.lower()
        user = User.get_by_auth_id(auth_id='own:' + email)        
        if user:
            game_name = webapp2.get_app().config['APP_INFO']['NAME']
            game_url = webapp2.get_app().config['APP_INFO']['URL']
            new_pass = security.generate_random_string(length=5)
            user.password = security.generate_password_hash(new_pass, length=12)
            try:                
                user.put()
            except:
                self.respond("0Password recovery failed. Please try again later.")
                return                

            subject = game_name + " login password recovery"
            body = """
Dear %s

This is an automated response. A request was made for your login password used with %s

Your new password is: %s

Use this new password to login to the game. You may change the password in your profile section.
For more information, visit %s

Thank you
""" % (user.name, game_name, new_pass, game_url)

            # send the email via tasqueue so this request can return now and not wait for mail api
            taskqueue.add(queue_name='prioritymail', url='/work/mailer/', params={
                        'email':email,
                        'subject':subject,
                        'body':body,
                        })
            
            if webapp2.get_app().debug:            
                self.respond("1<pre>"+body+"</pre>")
            else:
                self.respond("1")
            return
        
        else:
            self.respond("0We do not have a record of that e-mail address. You may register to join this game.")
            return
        
        self.respond("0")
                
    def register(self):
        # register a new player account
        email = self.get_post('em', '')
        name = self.get_post('nm', '')
        password = self.get_post('pw', '')
        
        if len(email)<3 or not game._email_re.match(email) or not mail.is_email_valid(email):
            self.respond("0Please enter a valid e-mail address. This is important to retrieve your password if you forget it."); return
        if len(password)<5 or len(password)>15:
            self.respond("0Please enter a password of between 5 and 15 characters."); return
        if len(name)<5 or len(name)>15 or not game._name_re.match(name):
            self.respond("0Please enter a public name of between 5 and 15 characters. Only letters and numbers allowed."); return
        
        email = email.lower()
        success, info = User.create_user(auth_id='own:' + email,
                                         unique_properties=['name_lower'],
                                         password_raw=password, 
                                         email=email,
                                         name=name,
                                         name_lower=name.lower()
                                         )
        if success:
            self.respond("1"); return
        else:
            if 'auth_id' in info: # email is used as auth_id/user/login name
                self.respond('0That e-mail address is in use. Use password recovery if you forgot your password.'); return
            if 'name_lower' in info:
                self.respond('0That public name is in use, please choose another one.'); return
        
        self.respond('0')
        
    def logout(self):
        if self.auth():
            auth.get_auth().unset_session()
        self.respond('1')  

    def settings(self):
        if not self.auth():
            self.respond('!'); return # not authenticated
            
        email_notify = int(self.get_post('email_notify', '-1'))
        
        if email_notify>=0:
            self.user.email_bmchallenge = (email_notify==1)
            try:
                self.user.put()
                self.respond("1"); return
            except:
                self.respond("0Failed to save settings."); return
                 
        self.respond("0Failed to save settings.")
        
    def enterkey(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return
        k = self.get_post('k', '0')
        self.out = '0Invalid gamekey (error:1)'
    
        if len(k)==12: # key must be 12 charas
            k = k.upper()
            q = PaypalTransaction.query(PaypalTransaction.gamekey==k)
            pp = q.get()            
            if pp: # check if key status valid and key not yet used              
                if pp.transaction_status==1 and len(pp.gamekey_used)==0:
                    # first check if player do not allready own the item
                    # note. only one item so hard coded to full game (1)
                    # when you add DLC and such you need to add more checks here t osee what must be unlcoked
                    if '1' not in self.user.shop:
                        try:
                            pp.gamekey_used = self.user.email # key is used
                            pp.put()
                            self.user.shop.append('1') # hard coded to bm1
                            self.user.put()
                            self.out = '11' # 1(result) 1(bm1 item)
                        except:
                            logging.error("Failed to use gamekey for: " + self.user.email + " - " + k)
                            self.respond('0Error while validating. Please contact support.'); return
                    else:
                        self.out = '0You allready own this item. Gamekey not used.'
                else:
                    self.out = '0Invalid gamekey (error:3)'
            else:
                self.out = '0Invalid gamekey (error:2)'
        self.respond()

class news(game.GameRequestHandler):
    def post(self):
        self.out = '0'
        q = News.query()
        q = q.order(-News.dt)
        res = q.fetch(5)
        
        if res:
            self.out = '1'
            for r in res:
                self.out += r.dt.strftime('%d %b') + '^'
                self.out += r.msg + '|'
                           
        self.respond()
        
class advert(game.GameRequestHandler):
    def post(self):
        self.out = '0'        
        # choose random advert
        q = Advert.query()
        res = q.fetch()
        if res:
            self.out = '1'
            r = random.randint(0, len(res)-1)
            self.out+=res[r].url

        self.respond()
                
class error(game.GameRequestHandler):
    def get(self):
        self.respond('!')
    def post(self):
        self.respond('!') 
                
class version(game.GameRequestHandler):
    # send client the game version
    def get(self):
        c = webapp2.get_app().config['APP_INFO']
        self.response.write('1' + c['VERSION'])
        
class mailer(webapp2.RequestHandler):
    def post(self):
        # processes mailing tasks
        sender_address = webapp2.get_app().config['APP_INFO']['NAME'] + " Support <"+webapp2.get_app().config['APP_INFO']['EMAIL_SENDER']+">"
        mail.send_mail(sender_address, 
                       self.request.get('email'), 
                       self.request.get('subject'),
                       self.request.get('body'), 
                       reply_to=webapp2.get_app().config['APP_INFO']['EMAIL_REPLY'])
        
