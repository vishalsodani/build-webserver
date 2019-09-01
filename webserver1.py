import socket

HOST, PORT = '', 13119

#what is AF_INET - Address Family , INET is for IPv4
# sock_stream means TCP
# SOCK_DGRAM means that it is a UDP socket.
#https://stackoverflow.com/a/1594039
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))
    
    http_response = b"""\
HTTP/1.1 200 OK

Hello World
"""
    client_connection.sendall(http_response)
    client_connection.close()


