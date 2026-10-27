from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"""
        <html>
          <head><title>Argo CD GitOps Demo</title></head>
          <body>
            <h1>Hello from Argo CD GitOps!</h1>
            <p>Deployed on Kubernetes using GitOps.</p>
          </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = HTTPServer(("0.0.0.0", int(os.getenv("PORT", "8080"))), Handler)
print("GitOps demo running on port 8080")
server.serve_forever()
