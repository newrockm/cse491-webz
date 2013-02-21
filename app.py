#! /usr/bin/env python
from wsgiref.simple_server import make_server

class SimpleApp(object):
    def __call__(self, environ, start_response):
        status = '200 OK'

        path = environ['PATH_INFO']

        if path == '/':
            content_type = 'text/html'
            data = """\
Visit:
<a href='content'>a file</a>,
<a href='error'>an error</a>,
<a href='helmet'>an image</a>,
<a href='somethingelse'>something else</a>
"""
        elif path == '/content':
            content_type = 'text/html'
            data = open('somefile.html').read()
        elif path == '/error':
            status = "404 Not Found"
            content_type = 'text/html'
            data = "Couldn't find your stuff."
        elif path == '/helmet':
            content_type = 'image/gif'
            data = open('Spartan-helmet-Black-150-pxls.gif', 'rb').read()
        elif os.path.exists('html/' + environ['PATH_INFO']):
            content_type = 'text/html'
            data = open('html/' + environ['PATH_INFO']).read();
        else:
            content_type = 'text/plain'
            data = "Hello, world; got path request %s" % environ['PATH_INFO']
        
        headers = [('Content-type', content_type)]
        start_response(status, headers)

        return [data]

if __name__ == '__main__':
    import random, socket, os
    port = random.randint(8000, 9999)
    
    app = SimpleApp()
    
    httpd = make_server('', port, app)
    print "Serving on port %d..." % port
    print "Try using a Web browser to go to http://%s:%d/" % \
          (socket.getfqdn(), port)
    httpd.serve_forever()
