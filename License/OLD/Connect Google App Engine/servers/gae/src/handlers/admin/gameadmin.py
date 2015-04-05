# -*- coding: utf-8 -*-
# 
# Created on 11 Aug 2011
# @author: PL Young
#=======================================================================================================================
        
import datetime
from ndb import model
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.auth import security
from wtforms import Form, IntegerField, TextField, TextAreaField, DateTimeField, BooleanField, validators
from game.models import News, Advert, User, PaypalTransaction 

#---------------------------------------------------------------------------------------------------------------------- 

context = {
    'title':'My Admin',
    'menu':[
        ('/_ah/myadmin/game/news','news'),
        ('/_ah/myadmin/game/adverts','adverts'),
        ('/_ah/myadmin/game/shop','shop'),
        ('/_ah/myadmin/game/gamekeys','gamekeys'),
    ]
}


class AdminRequestHandler(webapp2.RequestHandler):
    
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        rv = self.jinja2.render_template(_template, **context)        
        self.response.write(rv)

class index(AdminRequestHandler):
    def get(self):
        self.render_response("admin/index.html", **context)
        
    def post(self):
        self.render_response("admin/index.html", **context)      

#----------------------------------------------------------------------------------------------------------------------

class PaypalTransactionForm(Form):
    transaction_status = IntegerField(u'status (0/1)', default=1) 
    orig_query = TextAreaField(u'orig query', default='')
    transaction_id = TextField(u'transaction id', default='0')
    item_name = TextField(u'item name', default='1')
    payment_gross = TextField(u'payment gross', default='0')
    player_email = TextField(u'for player email', default='')
    customer_email = TextField(u'customer email', default='')
    customer_name = TextField(u'customer name', default='')
    gamekey = TextField(u'gamekey', default='')
    gamekey_used = TextField(u'used by', default='')
    
    def init_with_model(self, m):
        self.transaction_status.data=m.transaction_status
        self.orig_query.data=m.orig_query
        self.transaction_id.data=m.transaction_id
        self.item_name.data=m.item_name
        self.payment_gross.data=m.payment_gross
        self.player_email.data=m.player_email
        self.customer_email.data=m.customer_email
        self.customer_name.data=m.customer_name
        self.gamekey.data=m.gamekey
        self.gamekey_used.data=m.gamekey_used

class gamekeys(AdminRequestHandler):
    
    def __init__(self, request=None, response=None):
        context['title'] = 'Game :: GAMEKEYS'
        context['item_labels'] = ['date','status','item','gamekey','usedby','for','buyer','buyer_name','transaction']
        context['items'] = []
        self.initialize(request, response)
            
    def get(self, action=None):
        q = PaypalTransaction.query()
        q = q.order(-PaypalTransaction.purchasedate)
        res = q.fetch(20)
        for r in res:
            context['items'].append([r.key.urlsafe(), r.purchasedate, r.transaction_status, 
                                     r.item_name, r.gamekey, r.gamekey_used, r.player_email, r.customer_email,
                                     r.customer_name, r.transaction_id])                     
        self.render_response("admin/list.html", **context)               
                
    def post(self, action=None):
        if 'del_button' in self.request.POST and 'item_count' in self.request.POST:
            max_items = int(self.request.POST['item_count'])
            delkeys = []
            for i in range(1, max_items+1):
                k = 'key' + str(i)
                if k in self.request.POST:
                    delkeys.append(model.Key(urlsafe=self.request.POST[k]))
            if delkeys:
                model.delete_multi(delkeys)
            self.redirect('/_ah/myadmin/game/gamekeys')
            return
        
        context['edit_key'] = None
        form = PaypalTransactionForm()
            
        if 'edit_button' in self.request.POST:
            max_items = int(self.request.POST['item_count'])
            key = None
            for i in range(1, max_items+1):
                k = 'key' + str(i)
                if k in self.request.POST:
                    key = model.Key(urlsafe=self.request.POST[k])
                    break
            if key:
                pp = key.get()
                form.init_with_model(pp)
                context['edit_key'] = pp.key.urlsafe()                    
            else:
                self.redirect('/_ah/myadmin/game/gamekeys')   
                        
        if 'create_button' in self.request.POST or 'save_button' in self.request.POST:
            form = PaypalTransactionForm(self.request.POST)
            if form.validate():
                if 'save_button' in self.request.POST:
                    key = model.Key(urlsafe=self.request.POST['edit_key'])
                    trans = key.get()
                else: 
                    trans = PaypalTransaction()
                    
                trans.transaction_status = form.transaction_status.data 
                trans.orig_query = form.orig_query.data
                trans.transaction_id = form.transaction_id.data
                trans.item_name = form.item_name.data
                trans.payment_gross = form.payment_gross.data
                trans.player_email = form.player_email.data
                trans.customer_email = form.customer_email.data
                trans.customer_name = form.customer_name.data
                trans.gamekey = form.gamekey.data
                trans.gamekey_used = form.gamekey_used.data
                key = trans.put()
                
                if 'create_button' in self.request.POST and not trans.gamekey:
                    # was new transaction,, generate a gamekey 
                    trans.gamekey = str(key.id())
                    l = 12 - len(trans.gamekey)
                    if l > 0: 
                        trans.gamekey += security.generate_random_string(l).upper()
                    trans.put()
                    
                self.redirect('/_ah/myadmin/game/gamekeys')                
                    
        context['form'] = form
        self.render_response("admin/create.html", **context)
 
#----------------------------------------------------------------------------------------------------------------------

class NewsForm(Form):
    dt        = DateTimeField(u'Date')
    msg       = TextAreaField(u'Message', validators=[validators.Required()])
    
    def init_with_model(self, m):
        self.dt.data=m.dt
        self.msg.data=m.msg
            
class news(AdminRequestHandler):
    
    def __init__(self, request=None, response=None):
        context['title'] = 'Game :: NEWS'
        context['item_labels'] = ['date','message']
        context['items'] = []
        self.initialize(request, response)
            
    def get(self, action=None):
        q = News.query()
        q = q.order(-News.dt)
        res = q.fetch(20)
        for r in res:
            context['items'].append([r.key.urlsafe(), r.dt, r.msg])                     
        self.render_response("admin/list.html", **context)
                
    def post(self, action=None):
        if 'del_button' in self.request.POST and 'item_count' in self.request.POST:
            max_items = int(self.request.POST['item_count'])
            delkeys = []
            for i in range(1, max_items+1):
                k = 'key' + str(i)
                if k in self.request.POST:
                    delkeys.append(model.Key(urlsafe=self.request.POST[k]))
            if delkeys:
                model.delete_multi(delkeys)
            self.redirect('/_ah/myadmin/game/news')
            return
        
        context['edit_key'] = None
        form = NewsForm()
        form.dt.data = datetime.datetime.now() #.strftime('%Y-%m-%d %H:%M:%S')
        
        if 'edit_button' in self.request.POST:
            max_items = int(self.request.POST['item_count'])
            key = None
            for i in range(1, max_items+1):
                k = 'key' + str(i)
                if k in self.request.POST:
                    key = model.Key(urlsafe=self.request.POST[k])
                    break
            if key:
                unit = key.get()
                form.init_with_model(unit)
                context['edit_key'] = unit.key.urlsafe()                    
            else:
                self.redirect('/_ah/myadmin/game/news')   
                        
        if 'create_button' in self.request.POST or 'save_button' in self.request.POST:
            form = NewsForm(self.request.POST)
            if form.validate():
                if 'save_button' in self.request.POST:
                    key = model.Key(urlsafe=self.request.POST['edit_key'])
                    news = key.get()
                else: 
                    news = News()
                    
                news.dt=form.dt.data
                news.msg=form.msg.data
                news.put()
                
                self.redirect('/_ah/myadmin/game/news')                
                #form = NewsForm()                
                #if 'save_button' in self.request.POST:
                #    self.redirect('/_ah/myadmin/game/news')
                #    return
                    
        context['form'] = form
        self.render_response("admin/create.html", **context)
 
#----------------------------------------------------------------------------------------------------------------------

class AdvertForm(Form):    
    url = TextField(u'URL', validators=[validators.Required()])
    def init_with_model(self, m):
        self.url.data=m.url
            
class adverts(AdminRequestHandler):
    
    def __init__(self, request=None, response=None):
        context['title'] = 'Game :: ADVERTS'
        context['item_labels'] = ['url']
        context['items'] = []
        self.initialize(request, response)
            
    def get(self, action=None):
        q = Advert.query()
        res = q.fetch(20)
        for r in res:
            context['items'].append([r.key.urlsafe(), r.url])                     
        self.render_response("admin/list.html", **context)
                
    def post(self, action=None):
        if 'del_button' in self.request.POST and 'item_count' in self.request.POST:
            max_items = int(self.request.POST['item_count'])
            delkeys = []
            for i in range(1, max_items+1):
                k = 'key' + str(i)
                if k in self.request.POST:
                    delkeys.append(model.Key(urlsafe=self.request.POST[k]))
            if delkeys:
                model.delete_multi(delkeys)
            self.redirect('/_ah/myadmin/game/adverts')
            return
        
        context['edit_key'] = None
        form = AdvertForm()
        
        if 'edit_button' in self.request.POST:
            max_items = int(self.request.POST['item_count'])
            key = None
            for i in range(1, max_items+1):
                k = 'key' + str(i)
                if k in self.request.POST:
                    key = model.Key(urlsafe=self.request.POST[k])
                    break
            if key:
                unit = key.get()
                form.init_with_model(unit)
                context['edit_key'] = unit.key.urlsafe()                    
            else:
                self.redirect('/_ah/myadmin/game/adverts')   
                        
        if 'create_button' in self.request.POST or 'save_button' in self.request.POST:
            form = AdvertForm(self.request.POST)
            if form.validate():
                if 'save_button' in self.request.POST:
                    key = model.Key(urlsafe=self.request.POST['edit_key'])
                    news = key.get()
                else: 
                    news = Advert()
                    
                news.url=form.url.data
                news.put()
                
                self.redirect('/_ah/myadmin/game/adverts')
                #form = AdvertForm()                
                #if 'save_button' in self.request.POST:
                #    self.redirect('/_ah/myadmin/game/adverts')
                #    return
                    
        context['form'] = form
        self.render_response("admin/create.html", **context)
        
#---------------------------------------------------------------------------------------------------------------------- 

class UserFindForm(Form):
    email = TextField(u"Enter user's email ", validators=[validators.Required()])
    
class UserOwnsForm(Form):
    base_game = BooleanField(u"Base game ")

    def init_with_model(self, m):
        self.base_game.data = True if '1' in m.shop else False
    def update_model(self, m):
        if self.base_game.data==True:
            m.shop.append('1')
        
class shop(AdminRequestHandler):
    
    def __init__(self, request=None, response=None):
        context['title'] = 'Game :: SHOP'
        self.initialize(request, response)
            
    def get(self, action=None):
        form = UserFindForm()
        context['form'] = form
        self.render_response("admin/shop_index.html", **context)
                
    def post(self, action=None):
        if 'find_button' in self.request.POST:
            find_email = self.request.POST['email']
            q = User.query(User.email==find_email)
            user = q.get()
            if user:
                key = user.key.urlsafe()                
                if key:
                    form = UserOwnsForm()
                    form.init_with_model(user)
                    context['form'] = form
                    context['edit_key'] = key
                    context['player_name'] = user.name
                    self.render_response("admin/shop_edit.html", **context)        
                    return
                
        elif 'save_button' in self.request.POST:
            form = UserOwnsForm(self.request.POST)
            if form.validate():
                key = model.Key(urlsafe=self.request.POST['edit_key'])
                bmplayer = key.get()
                bmplayer.shop=['0']                    
                form.update_model(bmplayer)
                bmplayer.put()
                
        form = UserFindForm()
        context['form'] = form
        self.render_response("admin/shop_index.html", **context)        
        
#----------------------------------------------------------------------------------------------------------------------
