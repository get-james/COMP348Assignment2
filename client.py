import socket
import sys
import client_options
import pickle

HOST, PORT = "localhost", 9999
data = [1, "John"]

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # sock.sendall(bytes(data + "\n", "utf-8"))
    sock.send(pickle.dumps(data))

    # Receive data from the server and shut down
    received = pickle.loads(sock.recv(4096))

print("Sent:     {}".format(data))
print("Received: {}".format(received))