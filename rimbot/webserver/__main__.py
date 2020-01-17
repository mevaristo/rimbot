from . import config, functions, server, routes

if __name__ == "__main__":
    server.server.run(host='127.0.0.1',port='8090', debug=True)