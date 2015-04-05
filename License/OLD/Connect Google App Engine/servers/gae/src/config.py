# -*- coding: utf-8 -*-
# 
# Created on 31 Jul 2011
# @author: PL Young
#=======================================================================================================================

# !!! IMPORTANT !!!
# please search for CHANGE_ME and make the needed changes below

import logging
import os

logging.getLogger().setLevel(logging.DEBUG)
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

config = {   
    'APP_INFO': {
        'VERSION':          '000',                  # server/client version of game
        'NAME':             'Unity GAE sample app', # CHANGE_ME if you care to
        'AUTHOR':           'PL Young',             # CHANGE_ME if you care to
        'COMPANY':          'AwesomeCompInc',       # CHANGE_ME if you care to
        'EMAIL_SENDER':     'CHANGE_ME@gmail.com',  # MUST be same as login of an admin for app on GAE else emails cant be send by the app
        'EMAIL_REPLY':      'noreply@CHANGE_ME.com',# CHANGE_ME
        'URL':              'http://www.gameurl.com/', # CHANGE_ME if you care to
    },
    
    'webapp2_extras.sessions': {
        'secret_key': '91clEL8!0>Hk8LP3gjsSLBbsw1tUWm', # CHANGE_ME if you care to
    },

    'webapp2_extras.auth': {
        'user_model':       'game.models.User',
        'cookie_name':      'auth',
        'token_max_age':    172800,     # 2 days    
        'token_new_age':    86400,      # 1 day
        'token_cache_age':  3600,       # 1 hour
        'user_attributes':  [],
        'session_backend':  'securecookie'
    },
          
}

#=======================================================================================================================
#=======================================================================================================================
