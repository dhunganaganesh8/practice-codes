from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    greeting = request.args.get('greeting', 'Nobody')
    return f"Hello, {greeting}!"
