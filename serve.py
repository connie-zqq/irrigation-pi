#!/usr/bin/env python

import cherrypy
from irrigationpi import app, utils

utils.init_logging()

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(app.RootController(), '/')
