import socket


def run_server(ip: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    # print(f'Start server {server_socket.getsockname()}')
    print(f'Waiting message... ')
    try:
        conn, address = server_socket.accept()
        while True:
            received = conn.recv(1024)
            if not received:
                break
            data = received.decode()
            print(f'Message received from {address}: {data}')
            conn.send('OK'.encode())
        conn.close()
    except KeyboardInterrupt as err:
        print(f'Error: {err}. Destroy server')
    finally:
        server_socket.close()


if __name__ == '__main__':
    host = socket.gethostname()
    tcp_ip = socket.gethostbyname(host)
    tcp_port = 5000

    run_server(tcp_ip, tcp_port)
