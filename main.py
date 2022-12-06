import socket
from socket_client import run_client
from socket_server import run_server


if __name__ == '__main__':
    host = socket.gethostname()
    tcp_ip = socket.gethostbyname(host)
    tcp_port = 5000

    while True:
        value = input('1 - Send message. 2 - Receive message. 3 - Exit.: ')
        if value == '1':
            msg = input('>> ')
            run_client(tcp_ip, tcp_port, msg)
        elif value == '2':
            run_server(tcp_ip, tcp_port)
        elif value == '3':
            break
        else:
            print('Input error')
