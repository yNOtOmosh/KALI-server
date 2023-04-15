import socket
mySocket = socket.socket()
print("Socket successfully created")

#reserve a port on your computer eg 8080
port = 8080

#next is to bind to the port and have not typed an IP in the ip field
#keep the string empty; because this makes the server listen to any request coming from other computers on the network
mySocket.bind(("", port))
print("socket bounded to %s" % (port))

#put socket into listening mode
mySocket.listen(5)
print("socket is now listening")

#you can make it forever loop until we interrupt it or an error occurs
while True:
    #establish connection with client.
    c, addr = mySocket.accept()
    print('Got a connection from this', addr)

# we can send thank you message to client.
    c.send('Thank you for connecting')
    # close the connection with the client
    c.close
