# conding: utf-8

from wsgiref.simple_server import make_server, demo_app
def wsgi_application(environ, start_response):
    print('-'*30)
    status = '200 OK'
    response_header = [
    	('Content-type', 'text/html; charset=utf-8')
    ]
    start_response(status, response_header)
    
    response_body = '<h1>Hello Guizi!</h1><br />'
    for key, value in environ.items():
        response_body += '%s = %s <br />' % (key, value)
    return [response_body]




httpd = make_server('', 8000, wsgi_application)
print('Servering on Port 8000...')
httpd.serve_forever()
