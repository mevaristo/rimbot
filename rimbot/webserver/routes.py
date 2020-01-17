from . import server, functions

server.server.add_url_rule('/index', 'index', view_func=functions.home)

server.server.add_url_rule('/login', 'login', view_func=functions.login)
