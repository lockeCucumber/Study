# Standard library imports...
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import re
import socket
import cgi
from threading import Thread

# Third-party imports...
import requests


class MockServerRequestHandler(BaseHTTPRequestHandler):
    USERS_PATTERN = re.compile(r'/users')

    def do_GET(self):
        if re.search(self.USERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(requests.codes.ok)

            # Add response headers.
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            # Add response content.
            response_content = json.dumps([])
            self.wfile.write(response_content.encode('utf-8'))
            return

    def do_POST(self):
        if None != re.search('/api', self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                data = {"w":"we"}
                length = int(self.headers.getheader('content-length'))
                post_data = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
            else:
                data = {}
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        return

def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


def start_mock_server(port):
    mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()