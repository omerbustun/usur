from flask import Flask, render_template, request, redirect
from flask import request
from markupsafe import escape


#set FLASK_APP=app.py   - - - -   python -m flask run
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Test Run
# @app.route('/hello')
# def hello():
#     return "Hello"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'do login'
#     else:
#         return 'show_the_login_form'
        