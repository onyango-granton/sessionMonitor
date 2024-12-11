import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port of listening server
server_address =  ('localhost',4444)
print('connecting to "%s" port "%s"' % server_address)
# print >> sys.stderr, 'connecting to "%s" port "%s"' % server_address
sock.connect(server_address)

try:
    # send data
    message = 'This is the message am sending'
    print('sending', message)
    #print >> sys.stderr, 'sending', message
    sock.sendall(message.encode())

    # look for response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected: #same as while true
        data = sock.recv(16)
        amount_received += len(data)
        print("received ", data)
        #print >> sys.stderr, "received ", data
    
finally:
    print("closing socket")
    #print >> sys.stderr, "closing socket"
    sock.close()