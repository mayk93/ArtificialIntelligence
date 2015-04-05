# -*- coding: utf-8 -*-
# 
# Created on 31 Jul 2011
# @author: PL Young
#=======================================================================================================================

from ndb import model
from webapp2_extras.appengine.auth import models

# posisble values for the game and expansions a player can own in the game
# 0: free version, 1:base game, 2:todo-expansion
# IMPORTANT! Use single characters! 0,1,A,B,etc
BM_SHOP = ["0", "1"]

#---------------------------------------------------------------------------------------------------------------------- 
# Chat System Related

class ChatChannel(model.Model):
    created = model.DateTimeProperty(auto_now_add=True)     # date it was created
    pm_channel = model.BooleanProperty(default=False)       # if true, then only channel for two players
    uids = model.IntegerProperty(repeated=True)             # user IDs
    name = model.StringProperty(default='')                 # name for group channels, pm channels use player names  

    @classmethod
    def get_multi_by_id_async(cls, ids, **ctx_options):
        return [cls.get_by_id_async(i, **ctx_options) for i in ids]
  
    @classmethod
    def get_multi_by_id(cls, ids, **ctx_options):
        return [future.get_result() for future in cls.get_multi_by_id_async(ids, **ctx_options)]
    
class ChatMessage(model.Model):
    message = model.StringProperty()                # message, "player_name: some message"
    timestamp = model.IntegerProperty(default=0)    # timestamp of when msg was posted
    user_key = model.KeyProperty()                  # the user who posted the message
    cid = model.IntegerProperty(default=None)       # can be None, in which case message go onto public channel
        
    @classmethod
    def create(cls, user, message, timestamp, channel_id=None):
        message = user.name + ": " + message
        msg = cls(message=message, user_key=user.key, timestamp=timestamp, cid=channel_id)
        msg.put()
    
#---------------------------------------------------------------------------------------------------------------------- 
# Accounts System Related

class UserToken(models.UserToken):
    uid = model.IntegerProperty()                       # I need this when when a player is looking for opponents
    location = model.StringProperty(default='0')        # 0:on-website, L:lobby, G:in-game-playing,
    last_game_refresh = model.IntegerProperty(default=0)
    last_chat_refresh = model.IntegerProperty(default=0)
    plrname = model.StringProperty()                    # cached player name needed for player lists
    
class User(models.User):
    
    # additional fields to save for users
    email = model.StringProperty()
    name = model.StringProperty() 
    name_lower = model.StringProperty()                 # to make lookup easier    
    friends = model.IntegerProperty(repeated=True)      # list of friend UIDs
    signup_date = model.DateTimeProperty(auto_now_add=True)
    login_date = model.DateTimeProperty(auto_now=True)   
    shop = model.StringProperty(repeated=True, choices=BM_SHOP) # if player owns game and any expansions    
    email_bmchallenge  = model.BooleanProperty(default=False) # sample of a field holding settings rom the client. you could do saomething similar for game saves
    
    #set token model to use to the custom UserToken which contains aditional fields
    token_model = UserToken
        
    @classmethod
    def get_multi_by_id_async(cls, ids, **ctx_options):
        return [cls.get_by_id_async(i, **ctx_options) for i in ids]
  
    @classmethod
    def get_multi_by_id(cls, ids, **ctx_options):
        return [future.get_result() for future in cls.get_multi_by_id_async(ids, **ctx_options)]

#=======================================================================================================================
#=======================================================================================================================

class News(model.Model):
    dt = model.DateTimeProperty(auto_now_add=True)
    msg = model.TextProperty()
    
class Advert(model.Model):
    url = model.TextProperty()

class PaypalTransaction(model.Model):
        purchasedate = model.DateTimeProperty(auto_now_add=True)
        transaction_status = model.IntegerProperty(default=0)   # 0:validating or invalid, 1:completed 
        orig_query = model.TextProperty(default='')             # query that started transaction
        transaction_id = model.StringProperty(default='0')      # keep to prevent processing dupes
        item_name = model.StringProperty(default='fullgame')    # what was purchased
        payment_gross = model.StringProperty(default='0')       # how much was payed, should check and flag if not valid
        player_email = model.StringProperty(default='')         # the account for which game should be unlocked (or a key be send to)
        customer_email = model.StringProperty(default='')       # just incase player_email fails
        customer_name = model.StringProperty(default='')
        gamekey = model.StringProperty(default='')              # generated unlock key
        gamekey_used = model.StringProperty(default='')         # the email/account that used the key

#=======================================================================================================================
