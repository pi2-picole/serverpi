#!/usr/bin/python

import cherrypy

class ReleasePopsicle(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def index(self):
        popsicles = cherrypy.request.json
        print(popsicles)
        for key in popsicles.keys():
            release = popsicles[key]["release"]
            amount  = popsicles[key]["new_amount"]
            print(key, release, amount)
        return 'a'
        

if __name__ == '__main__':
    cherrypy.quickstart(ReleasePopsicle())

