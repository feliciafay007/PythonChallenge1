#!/usr/bin/env python 

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9876
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!" 

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((TCP_IP, TCP_PORT))
socket_client.send(MESSAGE)
data = socket_client.recv(BUFFER_SIZE)
socket_client .close()
print "client received data from server:", data

