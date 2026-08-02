import http.server
import functools
import os

DIRECTORY = "/Users/nana/Desktop/Code - Personal/Claude Code - Personal Use/Nana portfolio 2026"
PORT = int(os.environ.get("PORT", 8090))

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
httpd.serve_forever()
