from bottle import route, run
from bottle import get, post, request,redirect


@route('/', method='GET')
def defult():
    return "main"


run(host='localhost', port=8080, debug=True)