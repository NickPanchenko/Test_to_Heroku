from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello World!<p>'

if __name__ == '__main__':
    app.run()