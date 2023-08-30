from http import server

from assigner import provider

class RequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        print(self.__dict__)
        self.send_response(code=200)
        self.end_headers()
        uuid = provider.use_uuid()
        response = "{\"uuid\": \"" + uuid + "\"}"
        self.wfile.write(response.encode(encoding='utf_8'))