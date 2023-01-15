# def log(func):
#     def wrapper():
#         print("я слежу за тобой,функция!")
#         func()
#     return wrapper
#
# @log
# def another_func():
#     print("call smth")
#
#
# another_func()
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


app.run()
