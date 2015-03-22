# -*- coding: utf-8 -*-
# 
# Created on 03 Aug 2011
# @author: PL Young
#=======================================================================================================================

import time
import datetime
import game
from game.models import User, UserToken, ChatMessage, ChatChannel

max_players_list = 100 # max players to query for

#---------------------------------------------------------------------------------------------------------------------- 

class channel(game.GameRequestHandler):
    def post(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return
        
        name = self.get_post('u', '')
        channel_ids = self.get_post('n', '')
        
        self.out = '0' #default is error
        
        # player wants to join/create a private channel with another player    
        if name:
            # find the player's uid since I work with UIDs and not names
            q = User.query(User.name_lower == name.lower())
            user = q.get()
            if not user:
                self.respond('0'); return # not found                
            uid = int(user.get_id())            
            if uid == self.uid:
                self.respond('0'); return # cant PM self
                
            # first check if the channel between the two players dont exist, else create it
            # check for channel(s) where this user and target is in the uids and it is pm_channel 
            q = ChatChannel.query(ChatChannel.pm_channel == True, ChatChannel.uids == uid, ChatChannel.uids == self.uid)
            channel = q.get() # get first result
            if channel:
                # there is a channel, update its created date so it is fresh and then send it to player
                channel.created = datetime.datetime.now()
                channel.put()
                self.out = '1' + str(channel.key.id()) 
            else:
                # first check if requested user exist
                target = User.get_by_id(uid)
                
                # create the channel
                if target:
                    channel = ChatChannel(pm_channel = True, uids = [uid, self.uid] )
                    key = channel.put()
                    if key:
                        self.out = '1' + str(key.id())
            
        # player wants the names for channels
        elif channel_ids:
            
            sids = channel_ids.split(',')
            cids = [int(s) for s in sids if s]
            channels = ChatChannel.get_multi_by_id(cids) if cids else None
            if channels: 
                self.out = '1'
                for channel in channels:
                    
                    # send the name as is if the channel has one 
                    if channel.name:
                        self.out += '|' + str(channel.key.id()) + ',' + channel.name
                        
                    # else try and find the name it should be, prolly a player name for pm channel
                    else:
                        uid = 0 # find the other player's id in the list
                        for idd in channel.uids:
                            if idd != self.uid:
                                uid = idd
                                break
                        
                        if uid > 0:
                            player = User.get_by_id(uid)
                            if player:
                                self.out += '|' + str(channel.key.id()) + ',' + player.name  
        
        self.respond()

class messages(game.GameRequestHandler):
    def post(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return
        
        from_lobby = self.get_post('l', '1')   # L = 1:in-lobby, 0:somewhere-else-like-in-stage 
        msg_in = self.get_post('m', None)      # a message that was send by a player
        chan_in  = int(self.get_post('c', '0'))# chanel the message was send to
        
        # always reply with success code
        self.out = '1'
        timestamp = int(time.time())
        
        # save any message that player send            
        if msg_in:            
            # check if may post to the channel if trying to post to a channel            
            if chan_in > 0:                
                channel = ChatChannel.get_by_id(chan_in)
                if channel:
                    if self.uid in channel.uids:
                        # right, seems user may post to this channel
                        ChatMessage.create(user=self.user, message=msg_in, timestamp=timestamp, channel_id = chan_in)
                        
            # posting to public game channel
            else:
                ChatMessage.create(user=self.user, message=msg_in, timestamp=timestamp)
            
        # query for chat messages to send to the client
        q = ChatMessage.query(ChatMessage.timestamp > self.user_token.last_chat_refresh)
        q = q.order(ChatMessage.timestamp)
        res = q.fetch(100) # dont want more than this, hope they are slow chatters
                
        # send chat messages to the client
        if res:
            # im gonna check the msg timestamp to figure out the "last time" I checked for new msgs
            # cause when i just use time.now() it causes problems like msgs are missed or duplicates
            # grabbed depending on the use of > and >= in the ChatMessage.query
            #timestamp = 0
            
            for r in res:
                # I need this test since for GAE queries => Inequality Filters Are Allowed on One Property Only 
                # and I allready use inequality on the message timestamp
                if r.user_key != self.user.key:
                    self.out += '|' 
                    if r.cid:                        
                        self.out += '*' + str(r.cid) + '|'
                    self.out += r.message
                    #if r.timestamp > timestamp:
                    #    timestamp = r.timestamp 

        # update session
        self.user_token.last_chat_refresh = timestamp
        self.user_token.location = 'L' if from_lobby=='1' else 'G'
        self.user_token.put()

        self.respond()

class players(game.GameRequestHandler):
    def post(self):
        if not self.auth():
            self.respond('!') # not authenticated
            return

        self.out = '1'

        # find players online in past 2 minutes
        check_t = int(time.time() - 120) # 2 minutes
        q = UserToken.query(UserToken.last_chat_refresh >= check_t)
        q.order(-UserToken.updated)
        players = q.fetch(30)
        check_t = int(time.time() - 60) # 1 minutes
        for p in players:
            st = '1' # check if player is - 0:offline, 1:online, 2:bussy, 3:unknown
            if p.last_chat_refresh >= check_t:
                st = '1' # is online
                if p.location != 'L': # not in lobby
                    st = '2'
            self.out += '|' + str(p.uid) + ',' + st + ',' + p.plrname
                    
        self.respond()

#=======================================================================================================================
#=======================================================================================================================
