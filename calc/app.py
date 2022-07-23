# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'homepage'

@app.route('/add')
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a,b)
    return str(sum)

@app.route('/sub')
def subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)


@app.route('/mult')
def multiplication():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)


op = {
    "add" : add,
    "sub" : sub,
    "mult" : mult,
    "div" : div,
}

@app.route('/math/<operator>')
def math(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = op[operator](a,b)
    return str(result)