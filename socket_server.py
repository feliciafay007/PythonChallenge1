#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9876
BUFFER_SIZE = 1024

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((TCP_IP, TCP_PORT))
socket_server.listen(1)

while 1:
    conn, addr = socket_server.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    print "Server receive from client:", data
    conn.send("Hello Python : "+ data)  # echo
conn.close()
