import socket
import sys
from getClientData import parseData

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port of listening server
server_address =  ('localhost',4444)

print('connecting to "%s" port "%s"' % server_address)
sock.connect(server_address)

try:
    # send data
    message = parseData()
    print('sending', message)
    # converts string to bytes for transfer
    sock.sendall(message.encode())

    # look for response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("received ", data)
    
finally:
    print("closing socket")
    sock.close()