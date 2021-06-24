from gevent.pywsgi import WSGIServer
from app import app

http_server = WSGIServer(('127.0.0.1', 5005), app)
http_server.serve_forever()