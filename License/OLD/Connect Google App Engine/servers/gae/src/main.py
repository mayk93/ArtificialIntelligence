# -*- coding: utf-8 -*-
# 
# Created on 30 Jul 2011
# @author: PL Young
#=======================================================================================================================

import os
import sys

# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
lib_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib')
if lib_path not in sys.path:
    sys.path[0:0] = [lib_path,os.path.join(lib_path, 'dist'),os.path.join(lib_path, 'dist.zip'),]

#---------------------------------------------------------------------------------------------------------------------- 

import config
import urls
import webapp2

#---------------------------------------------------------------------------------------------------------------------- 

app = webapp2.WSGIApplication(routes=urls.routes, debug=True, config=config.config)

app.error_handlers[404] = 'handlers.error.handle'
app.error_handlers[500] = 'handlers.error.handle'


def main():
    app.run()
    
if __name__ == '__main__':
    main()

#=======================================================================================================================
#=======================================================================================================================
