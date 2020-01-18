from . import config, functions, server, routes

if __name__ == "__main__":
    print(server.server.url_map)