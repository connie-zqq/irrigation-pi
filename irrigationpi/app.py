import logging
import pathlib
import cherrypy
import sh


logger = logging.getLogger(__name__)


class RootController(object):
    @cherrypy.expose
    def index(self):
        return "Welcome! You just entered wonderland!"


@cherrypy.expose
class RFOutletController(object):

    def __init__(self, rf_outlet):
        self._rf_outlet = rf_outlet

    @cherrypy.tools.json_out()
    def GET(self):
        return self._rf_outlet.status()

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_out()
    def POST(self, operation):
        if operation in ('on', 'off'):
            getattr(self._rf_outlet, operation)()
            return self._rf_outlet.status()
        else:
            raise cherrypy.HTTPError(status=400, message="Doesn't support operation=" + str(operation))


class RFOutlet(object):
    def __init__(self, name, on_code, off_code, code_sender):
        self._name = name
        self._is_on = False
        self._on_code = on_code
        self._off_code = off_code
        self._code_sender = code_sender

    def on(self):
        logger.info("Sending code=%s to outlet=%s to turn it on", self._on_code, self._name)
        self._code_sender.send(self._on_code)
        self._is_on = True

    def off(self):
        logger.info("Sending code=%s to outlet=%s to turn it off", self._off_code, self._name)
        self._code_sender.send(self._off_code)
        self._is_on = False

    def status(self):
        return {"name": self._name, "status": "on" if self._is_on else "off"}


class RFCodeSender(object):
    def __init__(self):
        cur_class_dir = pathlib.Path(__file__).parent.absolute()
        codesender_path = cur_class_dir.parent.joinpath('bin', 'codesend')
        self._codesender = sh.Command(str(codesender_path))

    def send(self, code):
        self._codesender(code)
