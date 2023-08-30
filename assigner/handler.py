from http import server

from assigner.provider import provider

class RequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        print(self.__dict__)
        self.send_response(code=200)
        self.end_headers()
        response = "{\"uuid\": \"" + provider.select_then_update() + "\"}"
        self.wfile.write(response.encode(encoding='utf_8'))