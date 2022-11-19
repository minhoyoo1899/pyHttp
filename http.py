import http.server
import socketserver

PORT = 7878	#사용할 포트 입력

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()