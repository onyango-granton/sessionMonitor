import socket

def getHostName():
    return socket.gethostname()

def getIPAddr():
    return socket.gethostbyname(getHostName())

# works on linux
def getIP():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    return local_ip