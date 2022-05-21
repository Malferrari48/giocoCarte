__author__ = 'Malferrari e Ferrarini'

import CGIHTTPServer
import BaseHTTPServer
import os

os.chdir("../")


class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]


PORT = 8000

httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
