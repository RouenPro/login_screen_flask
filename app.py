from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return redirect('/login')

@app.route('/home')
def home():
    return 'login successful'

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        