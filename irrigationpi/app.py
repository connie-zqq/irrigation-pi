import cherrypy


class RootController(object):
    @cherrypy.expose
    def index(self):
        return "Welcome! You just entered wonderland!"
