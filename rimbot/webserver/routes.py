from . import functions
from .server import server

server.add_url_rule('/index', 'index', view_func=functions.home)

server.add_url_rule('/login', 'login', view_func=functions.login)

if __name__ == "__main__":
    print(server.url_map)