#!/usr/bin/env python

from bottle import request, run, route, Response

@route('/')
def index():
    return Response('Build: 3')

if __name__ == "__main__":
    run(host='0.0.0.0',
        port='3000',
        server='gunicorn',
        debug=True,
        reloader=True,
        workers=1)
