from traverse_current_directory import TraverseCurrentDir

class BrowserContentReader :
    def return_get(self, input_data):
        #print "input_data = ", input_data
        temp = ''.join((line + '\n') for line in input_data.splitlines()) 
        request_head, request_body = temp.split('\n\n', 1) 
        request_head = request_head.splitlines()
        request_headline = request_head[0]
        #print "request_headline = ", request_headline
        request_headers = dict(x.split(': ', 1) for x in request_head[1:])
        # headline has form of "POST /can/i/haz/requests HTTP/1.0"
        request_method, request_uri, request_proto = request_headline.split(' ', 3)
        print "REQUEST_METHOD : ", request_method, "\nREQUEST_URI : ", request_uri, "\nREQUEST_PROTO : ", request_proto, "\nREQUEST_HEADERS", request_headers, "\nREQUEST_BODY", request_body 
        return request_method, request_uri, request_proto, request_body, request_headers
        
    """
    for Milestone 2, return a static web page
    """
    def return_body(self, request_method, request_uri, request_proto, request_body, request_headers, client_sock):
        response_body = [
            '<html><body><h1>Hello, Python Challenge Milestone 2!</h1>',
            '<p>This page is in location %(request_uri)r, was requested ' % locals(),
            'using %(request_method)r, and with %(request_proto)r.</p>' % locals(),
            '<p>Request body is %(request_body)r</p>' % locals(),
            '<p>Actual set of headers received:</p>',
            '<ul>',]

        for request_header_name, request_header_value in request_headers.iteritems():
            response_body.append('<li><b>%r</b> == %r</li>' % (request_header_name, \
                                                    request_header_value))
        response_body.append('</ul></body></html>')
        response_body_raw = ''.join(response_body)

        # Clearly state that connection will be closed after this response,
        # and specify length of response body
        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.iteritems())

        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK' # this can be random

        # sending all this stuff
        client_sock.send('%s %s %s' % (response_proto, response_status, \
                                                        response_status_text))
        client_sock.send(response_headers_raw)
        client_sock.send('\n') # to separate headers from body
        client_sock.send(response_body_raw)

        # and closing connection, as we stated before
        client_sock.close()
        return 


    """
    for Milestone 3, return current directory traversal
    """
    def return_current_dir(self, request_method, request_uri, request_proto, request_body, request_headers, client_sock, dir_name):
        response_body = [
            '<html><body><h1>Hello, Python Challenge Milestone 3!</h1>',
            '<p>This page is in location %(request_uri)r, was requested ' % locals(),
            '<p>current dir is :</p>',
            '<ul>',]

        traverse = TraverseCurrentDir() 
        RESULT_IS_OK, current_dir_list = traverse.files_in_cur_dir(request_uri)

        for each in current_dir_list:
            response_body.append('<li><b>%s</b></li>'% (each))

        response_body.append('</ul></body></html>')
        response_body_raw = ''.join(response_body)

        # Clearly state that connection will be closed after this response,
        # and specify length of response body
        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.iteritems())

        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK' # this can be random

        if RESULT_IS_OK == -1 :
            response_status = '404'
            response_status_text = 'Error code 404, Page Not Found!' # this can be random

        # sending all this stuff
        client_sock.send('%s %s %s' % (response_proto, response_status, \
                                                        response_status_text))
        client_sock.send(response_headers_raw)
        client_sock.send('\n') # to separate headers from body
        client_sock.send(response_body_raw)

        # and closing connection, as we stated before
        client_sock.close()
        return 



    """
    for Milestone 4, return current directory traversal, with hyperlink attached.
    """
    def return_current_dir_and_link(self, request_method, request_uri, request_proto, request_body, request_headers, client_sock, dir_name):
        response_body = [
            '<html><body><h1>Hello, Python Challenge Milestone 4!</h1>',
            '<p>This page is in location %(request_uri)r, was requested ' % locals(),
            '<p>current dir is :</p>',
            '<ul>',]

        traverse = TraverseCurrentDir() 
        RESULT_IS_OK, file_list , hyper_link= traverse.files_and_links_in_cur_dir(dir_name)
        
        for each in range(0, len(file_list)):
            if (hyper_link[each] != '-') :         
                response_body.append('<li><a href="%s"><b>%s</b></a></li> ' % (hyper_link[each], file_list[each]))
            else:
                response_body.append('<li><b>%s</b></li> ' % (file_list[each]))

        response_body.append('</ul></body></html>')
        response_body_raw = ''.join(response_body)

        # Clearly state that connection will be closed after this response,
        # and specify length of response body
        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.iteritems())

        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK' # this can be random

        if RESULT_IS_OK == -1 :
            response_status = '404'
            response_status_text = 'Error code 404, Page Not Found!' # this can be random

        # sending all this stuff
        client_sock.send('%s %s %s' % (response_proto, response_status, \
                                                        response_status_text))
        client_sock.send(response_headers_raw)
        client_sock.send('\n') # to separate headers from body
        client_sock.send(response_body_raw)

        # and closing connection, as we stated before
        client_sock.close()
        return 

