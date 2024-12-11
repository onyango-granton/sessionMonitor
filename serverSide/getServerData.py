import socket

def getHostName():
    return socket.gethostname()

def getIPAddr():
    return socket.gethostbyname(getHostName())