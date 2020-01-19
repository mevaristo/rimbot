from flask import request, render_template, flash, url_for, redirect, Flask
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
            form.username.data, form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', form = login_form)


"""
def load_home():
    return render_template('index.html')



def do_login():
    pass

def load_panel():
    pass

"""