
from assigner.handler import RequestHandler
from assigner import provider
from assigner.server import Server

if __name__ == "__main__":
  provider.create_uuids()
  server_address = ('', 8000)
  httpd = Server(server_address, RequestHandler)
  print('Server Running')
  httpd.serve_forever()