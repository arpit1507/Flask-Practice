from flask import Flask, render_template,request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my website!"

@app.route('/index', methods=['GET'])
def index():
    return "welcome to the index page!"

@app.route('/sucess/<int:score>', methods=['GET'])
def sucess(score):
    return "Congratulations! You scored " + str(score) + "!"

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        retrunmessage = "Thank you " + name + "! Your email is " + email + " and your message is " + message + "!"
        return render_template('form.html', message=retrunmessage)

@app.route('/api', methods=['POST'])
def calculate_sum()
    data= request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jasonify({'sum': a_val + b_val})


if __name__ == '__main__':
    app.run(debug=True)