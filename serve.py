#!/usr/bin/env python
import pathlib
import cherrypy
from irrigationpi import config, app, utils

utils.init_logging()
_water_pump_rf_outlet = app.RFOutlet('water-pump',
                                     config.water_pump_outlet_codes[0],
                                     config.water_pump_outlet_codes[1],
                                     app.RFCodeSender())
_water_pump_controller = app.RFOutletController(_water_pump_rf_outlet)
app.setup_cronjob(_water_pump_rf_outlet, config.water_pump_cron_settings)
app.scheduler.start()

root_conf = {
    '/': {
        'tools.sessions.on': True,
        'tools.staticdir.root': pathlib.Path(__file__).parent.absolute()
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './static'
    }
}

api_conf = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'application/json')],
        'tools.encode.on': True,
        'tools.encode.encoding': 'utf-8',
        'tools.encode.text_only': False
    }
}

cherrypy.server.socket_host = '0.0.0.0'

cherrypy.tree.mount(app.RootController(), '/', root_conf)
cherrypy.tree.mount(_water_pump_controller, '/api/water-pump', api_conf)

cherrypy.engine.start()
cherrypy.engine.block()
