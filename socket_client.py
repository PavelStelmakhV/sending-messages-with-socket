import socket


def run_client(ip: str, port: int, message: str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ip, port))
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        if response == 'OK':
            print('Message successfully delivered')
        else:
            print(f'Message not delivered. Server send {response}')
    except KeyboardInterrupt as err:
        print(f'Message not delivered. Error: {err}.')
    except ConnectionRefusedError as err:
        print(f'Message not delivered. Error: {err}.')
    finally:
        client_socket.close()


if __name__ == '__main__':
    host = socket.gethostname()
    tcp_ip = socket.gethostbyname(host)
    tcp_port = 5000
    msg = 'first message'
    run_client(tcp_ip, tcp_port, msg)
