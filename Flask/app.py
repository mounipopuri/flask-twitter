from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import sys,os

app = Flask(__name__)
app.config['SECRET_KEY']

@app.route('/')
def nav():
	return render_template('firstpage.html')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        user= request.form['username']
        pas=request.form['password']
        if user=="mounika" and pas=="mounika":
            session['user']=request.form['username']
            return render_template('index.html')
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/items')
def items():
    return render_template('items.html')
@app.route('/additems')
def additems():
	return render_template('')
@app.route('/')
def logout():
	return render_template('index.html')

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)

    
    