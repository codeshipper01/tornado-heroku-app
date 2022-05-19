#!usr/bin/env python

import os

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

def make_app():
    return tornado.web.Application([
    (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.listen(int(os.environ.get("PORT", 5000)))
    else:
        app.listen(8888)
    tornado.ioloop.IOLoop.current().start()