# -*- coding: utf-8 -*-
# 
# Created on 31 Jul 2011
# @author: PL Young
#=======================================================================================================================

import logging
import webapp2
import traceback

def handle(request, response, exception):
    logging.exception(exception)
        
    if isinstance(exception, webapp2.HTTPException):
        response.set_status(exception.code)
    else:
        response.set_status(500)      
    
    response.write("!")
    
    if webapp2.get_app().debug:
        response.write("<pre>%s</pre>" % traceback.format_exc())

#=======================================================================================================================
#=======================================================================================================================
