from http.server import BaseHTTPRequestHandler
# from main import main


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # start up client, wait until command completion, return, continue
        # TODO: move code from main to here
        # main()
        print('GET reached')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
