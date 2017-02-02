import SocketServer
import CGIHTTPServer 
Handler = CGIHTTPServer.CGIHTTPRequestHandler
PORT = 8000

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()