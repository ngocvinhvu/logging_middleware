from flask import Flask, request
from logging_middleware import logging_request, logging_response

app = Flask(__name__)
app.config.from_object('config')

#main
app.before_request(logging_request)
app.after_request(logging_response)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return {1: 'hello'}

app.run(debug=True)
