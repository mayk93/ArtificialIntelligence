# -*- coding: utf-8 -*-
# 
# Created on 31 Jul 2011
# @author: PL Young
#=======================================================================================================================

from webapp2 import Route

routes = [

    # CHAT AREA RELATED
    Route(r'/msgs/',       handler='handlers.chat.messages',               methods=['POST']),
    Route(r'/cpm/',        handler='handlers.chat.channel',                methods=['POST']),
    
    # FRIENDS AND PLAYERS
    Route(r'/listp/',      handler='handlers.chat.players',                methods=['POST']),
    Route(r'/delf/',       handler='handlers.friends.delete',              methods=['POST']),
    Route(r'/addf/',       handler='handlers.friends.add',                 methods=['POST']),
    Route(r'/listf/',      handler='handlers.friends.listf',               methods=['POST']),

    # ACCOUNTS RELATED
    Route(r'/logout/',     handler='handlers.gamecommon.account:logout',   methods=['POST']),
    Route(r'/login/',      handler='handlers.gamecommon.account:login',    methods=['POST']),    
    Route(r'/reg/',        handler='handlers.gamecommon.account:register', methods=['POST']),
    Route(r'/rpw/',        handler='handlers.gamecommon.account:recoverpw',methods=['POST']),
    Route(r'/cpw/',        handler='handlers.gamecommon.account:changepw', methods=['POST']),
    Route(r'/settings/',   handler='handlers.gamecommon.account:settings', methods=['POST']),
    Route(r'/key/',        handler='handlers.gamecommon.account:enterkey', methods=['POST']),
    
    # MISC
    Route(r'/news/',       handler='handlers.gamecommon.news',             methods=['POST']),
    Route(r'/aimg/',       handler='handlers.gamecommon.advert',           methods=['POST']),
    Route(r'/ver/',        handler='handlers.gamecommon.version',          methods=['GET']),    
    
    # ADMIN
    Route(r'/_ah/myadmin/game',         handler='handlers.admin.gameadmin.index'),
    Route(r'/_ah/myadmin/game/news',    handler='handlers.admin.gameadmin.news'),
    Route(r'/_ah/myadmin/game/adverts', handler='handlers.admin.gameadmin.adverts'),
    Route(r'/_ah/myadmin/game/shop',    handler='handlers.admin.gameadmin.shop'),
    Route(r'/_ah/myadmin/game/gamekeys',handler='handlers.admin.gameadmin.gamekeys'),
    
    # PAYMENT HANDLERS
    Route(r'/pay_pp/',          handler='handlers.payment.paypal'),
        
    # TASKS
    Route(r'/work/pay_pp1/',    handler='handlers.payment.paypal_task_processor1'),
    Route(r'/work/pay_pp2/',    handler='handlers.payment.paypal_task_processor2'),
    Route(r'/work/mailer/',     handler='handlers.gamecommon.mailer'),
    
    # CATCH-ALL
    Route(r'/', name='home',    handler='handlers.gamecommon.error'),
]

#=======================================================================================================================
