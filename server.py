import socketserver
import server_functions
import pickle

server_functions.file_reader()
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.received_data = pickle.loads(self.data)
        print(self.received_data)
        self.database_entry = (self.received_data)
        self.database_entry = server_functions.data_reader(self.database_entry)
        #   print("{} wrote:".format(self.client_address[0]))
        # print(self.data)
        # just send back the same data, but upper-cased
        self.request.send(pickle.dumps(self.database_entry))
       
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()




