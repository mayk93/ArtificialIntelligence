# -*- coding: utf-8 -*-
# 
# Created on 03 Aug 2011
# @author: PL Young
#=======================================================================================================================

import time
import game
from game.models import User, UserToken

#---------------------------------------------------------------------------------------------------------------------- 

class listf(game.GameRequestHandler):
    def post(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return
        self.out = '0'
        if self.user.friends:
            players = User.get_multi_by_id(self.user.friends)
            if players:
                # now lookup statuses
                check_t = int(time.time() - 90) # 1.5 minutes
                q = UserToken.query(UserToken.uid.IN(self.user.friends), UserToken.last_chat_refresh >= check_t)
                q.order(-UserToken.updated)
                tokens = q.fetch()
                
                self.out = '1'
                for p in players:
                    uid = int(p.get_id())
                    st = '0' # check if player is - 0:offline, 1:online, 2:bussy, 3:unknown
                    if tokens:
                        for t in tokens:
                            if t.uid == uid:
                                st = '1' # is online
                                if t.location != 'L': # not in lobby
                                    st = '2' # but is bussy (ingame)
                                break
                                            
                    self.out += '|' + str(uid) + ',' + st + ',' + p.name
                    
        self.respond()

class add(game.GameRequestHandler):
    def post(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return
        name = self.get_post('u', '')
        self.out = '0'
        
        if name:
            # find the player's uid since I work with UIDs and not names
            q = User.query(User.name_lower == name.lower())
            user = q.get()
            if not user:
                self.respond('0'); return # not found                
            uid = int(user.get_id())            
            if uid == self.uid:
                self.respond('0'); return # cant add self
            
            self.out = '1'
            # check if not allready in friend list
            if self.user.friends:
                for f in self.user.friends:
                    if f == uid:
                        self.respond('1'); return;  # found the friend in list, return
                self.user.friends.append(uid)       # not found ,add
                self.out += str(uid) + ',' + user.name
            else: 
                self.user.friends = [uid]           # create list since it was None
                self.out += str(uid) + ',' + user.name
            
            self.user.put() # save

        self.respond()
        
class delete(game.GameRequestHandler):
    def post(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return
        uid = int(self.get_post('u', '0'))
        if uid>0:
            try:
                self.user.friends.remove(uid) # remove first item with this value (uid)
                self.user.put()
            except:
                pass
            finally:
                self.respond('1')
                
        self.respond('1')

#=======================================================================================================================
#=======================================================================================================================
