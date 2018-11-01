from bottle import route, run
from bottle import get, post, request,redirect


@route('/', method='GET')
def defult():
    test = "test"
    test = 12345

    return test


run(host='0.0.0.0', port=8080)