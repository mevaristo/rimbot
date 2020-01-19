"""
from flask import Flask, render_template



server = Flask(__name__)

@server.route('/login')
def login():
    return render_template('login.html')

@server.route('/index')
def index():
    return render_template('index.html')
"""

from rimbot.webserver.server import server
from rimbot.config import Config

server.config.from_object(Config)

if __name__ == "__main__":
    server.run(host='127.0.0.1',port='8090', debug=True)
