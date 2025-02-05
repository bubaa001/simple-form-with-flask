from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "hello"


@app.route('/hello')

def hello():
    return " hello, mumaa"


if __name__ == '__main__':
    app.run(debug=True)