# A basic python web server that serves index.html

import http.server
import socketserver

HOST = "localhost"
PORT = 3000

class Handler (http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
            super().do_GET()
        elif self.path == "/test":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello World"
            self.wfile.write(message.encode())
        else:
            self.send_error(404, "File not found")
    


if __name__ == "__main__":
    web_server = http.server.HTTPServer((HOST, PORT), Handler)
    print("serving at port", PORT)
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server closed.")
