import socket
import getServerData
import os

# creating a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get server IP
serverIP = getServerData.getIPAddr()

# binding the socket to the port
#server_address = (serverIP,4444)

# for some reason serverIP for linux is 127.0.0.1

server_address = ('localhost',4444)

print("Starting up on %s port %s", server_address)
sock.bind(server_address)

#listening for incoming connection
sock.listen(1)

#loop to wait for connection
while True:
    print("Waiting for connection")
    connection, client_address = sock.accept()

# connection is set now handling data
    try:
        print('connection from', client_address)

        #check if path exsists if not create it
        if os.path.exists("dataCleaning/receivedLogs/") == False:
            os.system("mkdir dataCleaning/receivedLogs/")

        #open receivedFile
        clientFile = open("dataCleaning/receivedLogs/"+client_address[0]+".txt", 'w')
        while True:
            # receive the data in small chunks
            data = connection.recv(16)
            print('received %s' % data)
            # data is decoded from bytes to utf-8 string
            clientFile.write(data.decode('utf-8'))

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
        clientFile.close()
        connection.close()
        os.system("go run dataCleaning/main.go")

        