from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
    
    def log_message(self, format, *args):
        pass

def run_server():
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting backend server on port 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
