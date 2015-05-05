#!/usr/bin/env python

import socket
from browser_content_reader import BrowserContentReader
TCP_IP = '127.0.0.1'
TCP_PORT = 9876
BUFFER_SIZE = 1024

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((TCP_IP, TCP_PORT))
socket_server.listen(1)

"""
for milestone 2 .
use a class to analyze the received content from browser.
"""

while 1:
    conn, addr = socket_server.accept()
    print "CONNECTION ADDRESS : " , addr
    data = conn.recv(BUFFER_SIZE)
    bc = BrowserContentReader()
    request_method, request_uri, request_proto, request_body, request_headers  = bc.return_get(data)
    #print "RECEIVED_FROM_CLIENT : ", data
    #print "RECEIVED_FROM_CLIENT_HEADER : ", header_from_bc
    #bc.return_body(request_method, request_uri, request_proto, request_body, request_headers, conn)
     
    bc.return_current_dir_and_link(request_method, request_uri, request_proto, request_body, request_headers, conn, request_uri)
conn.close()
