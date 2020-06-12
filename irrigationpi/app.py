import logging
import pathlib
import cherrypy
import sh


logger = logging.getLogger(__name__)


class RootController(object):
    @cherrypy.expose
    def index(self):
        return "Welcome! You just entered wonderland!"


class RFCodeSender(object):
    def __init__(self):
        cur_class_dir = pathlib.Path(__file__).parent.absolute()
        codesender_path = cur_class_dir.parent.joinpath('bin', 'codesend')
        self._codesender = sh.Command(str(codesender_path))

    def send(self, code):
        self._codesender(code)
