# -*- coding: utf-8 -*-
# 
# Created on 30 Jul 2011
# @author: PL Young
#=======================================================================================================================

import re
import logging
import webapp2
import traceback
from webapp2_extras import sessions
from webapp2_extras import auth
from game.models import User, UserToken

#---------------------------------------------------------------------------------------------------------------------- 

# regex to check usernames and public names against
_name_re = re.compile(r"^[\w.-]+$", re.IGNORECASE)
_email_re = re.compile(r"^.+@[^.].*\.[a-z]{2,10}$", re.IGNORECASE)

class GameRequestHandler(webapp2.RequestHandler):
    
    user = None         # game.models.User
    user_token = None   # game.models.UserToken ('auth')
    uid = 0             # int of this user's id user_token.user / user.get_id() / session_data['user_id']
    out = '0'           # the response will be saved in here to be send via respond()
                        # this is so I can change how data is send in one place if I wanna encode later
    
    def handle_exception(self, exception, debug):
        logging.exception(exception)
        if isinstance(exception, webapp2.HTTPException):
            self.response.set_status(exception.code)
        else:
            self.response.set_status(500)
        self.response.write('!') # dont send a '0' so that it do not look like normal error to the game client
        if webapp2.get_app().debug:    
            self.response.write("<pre>%s</pre>" % traceback.format_exc())
                
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
    
    #@webapp2.cached_property
    #def session_store(self):
    #    return sessions.get_store(request=self.request)
                   
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
                
    def auth(self):
        """ checks if user is loged in """
        if not self.user:
            data = auth.get_auth().get_session_data()
            if data:
                self.user_token = UserToken.get(user=data['user_id'], subject='auth', token=data['token'])
                if self.user_token:
                    self.user = User.get_by_id(data['user_id'])
                    self.uid = int(self.user.get_id())
                        
        return self.user != None and self.user_token != None
            
    def get_post(self, key, default):
        if key in self.request.POST:
            return self.request.POST[key]
        return default
                                        
    def respond(self, value=None):
        if value:
            self.out = value
        self.response.write(self.out)

#=======================================================================================================================
