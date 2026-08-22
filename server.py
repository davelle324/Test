import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()


port = int(os.environ.get("PORT", 10000))
print(f"Serving on port {port}")
HTTPServer(("", port), CORSHandler).serve_forever()
