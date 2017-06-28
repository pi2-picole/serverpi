#!/usr/bin/python3

import cherrypy
from subprocess import call

cherrypy.config.update({'server.socket_host': "192.168.43.243",
						'server.socket_port': 8080,
					   })

class ReleasePopsicle(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def index(self):
		popsicles = cherrypy.request.json
		print(popsicles)
		a = 0;		
		b = 0;		
		c = 0;		
		d = 0;		
		for key in popsicles.keys():
			if (int(key) == 1):
				a = int(popsicles[key]["release"])
			if (int(key) == 2):
				b = int(popsicles[key]["release"])
			if (int(key) == 3):
				c = int(popsicles[key]["release"])
			if (int(key) == 4):
				d = int(popsicles[key]["release"])
		call("./rodar_motor {} {} {} {}".format(a,b,c,d).split())
		return ''
		

if __name__ == '__main__':
	cherrypy.quickstart(ReleasePopsicle())
