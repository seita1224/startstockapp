from bottle import route, run
from bottle import get, post, request,redirect


@route('/', method='GET')
def defult():

    return "StartStockApp"


run(host='0.0.0.0', port=8080)