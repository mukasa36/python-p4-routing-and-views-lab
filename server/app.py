#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route("/count/<int:count>")
def count(count):
    print(count)
    mylist=[ x for x in range(1,count+1)]
    print("this is my values ",mylist)

    return f"{mylist}" 

@app.route("/math/<int:num1>/<operation>/<int:num2>")

def math(num1,operation,num2):
    if operation== "+":
        sum =num1+num2
        return f"<h1>{sum}</h1>"
    elif operation =="-":
        minus =num1 -num2
        return f"<h1>{minus}</h1>"
    elif operation == "*":
        multiply =num1 *num2
        return f"<h1>{multiply}</h1>"
    elif operation =="div":
        divide =num1 /num2
        return f"<h1>{divide}</h1>"

    elif operation =="%":
        modulus=num1%num2
        return f"<h1>{modulus}</h1>" 
    else :
        return f"<h1> verify  the operations</h1>"





