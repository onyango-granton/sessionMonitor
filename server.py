# socket is ip:port
# tcp data ftp file
import socket
import sys

# creating a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the socket to the port
server_address =  ('localhost',4444)
print("Starting up on %s port %s", server_address)
sock.bind(server_address)

#listening for incoming connection
sock.listen(1)

#loop to wait for connection
while True:
    print("Waiting for connection")
    #print >>sys.stderr, "Waiting for connection"
    connection, client_address = sock.accept()

# connection is set now handling data
    try:
        print('connection from', client_address)
        #print >> sys.stderr, 'connection from', client_address

        #open receivedFile
        clientFile = open(client_address[0]+".txt", 'a')
        while True:
            # receive the data in small chunks
            data = connection.recv(16)
            print('received %s' % data)
            clientFile.write(data.decode('utf-8'))
            #print >> sys.stderr, 'received %s' % data

            
            # sending data to client
            if data:
                print("sending data back to client")
                #print >> sys.stderr, "sending data back to client"
                connection.sendall(data)
                
            else:
                print('no more data from', client_address)
                #print >> sys.stderr, 'no more data from', client_address
                break
    
    finally:
        # clean up the connection
        connection.close()