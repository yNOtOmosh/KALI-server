#how to connect to google by using the socket programming in python

import socket
import sys

try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

except socket.error as err:
    print("socket creation failed with error %s" % (err))

    #default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('ww.google.com')
except socket.gaierror:

    #this means could not resolve the host
    print("there was an error resolving the host")

    sys.exit()

#connecting to the server
mySocket.connect((host_ip, port))

print("the socket has successfully connected to google on port == %s" % (host_ip))
