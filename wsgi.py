#!/usr/bin/env python

from bottle import run, route, Response

@route('/')
def index():
    return Response('Build: 8')

if __name__ == "__main__":
    run(host='0.0.0.0',
        port='3000',
        server='gunicorn',
        debug=True,
        reloader=True,
        workers=1)
