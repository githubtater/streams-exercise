#!/usr/bin/env python3

import socket

# Create server object using given URL
server = socket.getaddrinfo('hasthelargehadroncolliderdestroyedtheworldyet.com', 'http')
print(server)

# Create a client for connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client.connect(('216.92.96.71', 80))

# Construct the message
msg = "GET / HTTP/1.1\r\n"
msg += "Host: hasthelargehadroncolliderdestroyedtheworldyet.com\r\n\r\n"
msg = msg.encode('utf8')

# Sockets can only send bytes, never unicode
# print(client.send(msg))
# response = client.recv(75)
# print(response)
print(client.recv(client.send(msg)))


# Always close the connection once finished.
client.close()

