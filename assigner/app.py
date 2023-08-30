
from assigner.handler import RequestHandler
from assigner.provider import provider
from assigner.server import Server

if __name__ == "__main__":
  provider.load_uuids()
  server_address = ('', 8000)
  httpd = Server(server_address, RequestHandler)
  print('Server Running')
  httpd.serve_forever()