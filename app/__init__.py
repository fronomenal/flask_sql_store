from app.server import server

if __name__ == "__main__":
    server.run(host="localhost", port=8080, debug=True)