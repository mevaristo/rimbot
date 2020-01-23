from flask import request, render_template
from flask import flash, url_for, redirect
from flask import Flask, make_response
from flask import abort

from rimbot.webserver.forms import LoginForm

server = Flask(__name__)

@server.route('/index')
def index():
    return render_template('index.html')

@server.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', form = login_form)


"""
def load_home():
    return render_template('index.html')



def do_login():
    pass

def load_panel():
    pass

"""