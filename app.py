from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my website!"

@app.route('/index', methods=['GET'])
def index():
    return "welcome to the index page!"

if __name__ == '__main__':
    app.run(debug=True)