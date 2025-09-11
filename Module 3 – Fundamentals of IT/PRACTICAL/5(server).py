# LAB EXERCISE
# Simple HTTP Client-Server Communication (Python Example)

import http.server
import socketserver

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
