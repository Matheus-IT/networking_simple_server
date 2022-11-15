"""
Integrantes:
    Matheus da Costa da Silva
    Thiago Vinicios Sousa
"""

import socket


def client():
    """This is the main function for the client"""
    hostname = socket.gethostname()
    server_socket_port = 8000

    implementation_choices = {
        '1': use_tcp_socket_implementation,
        '2': use_udp_socket_implementation,
    }

    choice = input('Qual implementação deseja usar? (1-TCP | 2-UDP) -> ')

    use_chosen_socket_implementation = implementation_choices[choice]

    use_chosen_socket_implementation(hostname, server_socket_port)


def use_tcp_socket_implementation(hostname, server_socket_port):
    instantiate_tcp_socket = lambda: socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )
    with instantiate_tcp_socket() as client_socket:
        # connecting to the server
        client_socket.connect((hostname, server_socket_port))

        END_MESSAGE = 'tchau'

        while True:
            message = input(f'Digite alguma coisa ("{END_MESSAGE}" para sair) -> ')
            if message.lower().strip() == END_MESSAGE:
                break

            client_socket.send(message.encode())

            data = client_socket.recv(1024).decode()
            present_received_from_server(data)


def use_udp_socket_implementation(hostname, server_socket_port):
    instantiate_udp_socket = lambda: socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM,
    )
    with instantiate_udp_socket() as client_socket:
        END_MESSAGE = 'tchau'

        while True:
            message = input(f'Digite alguma coisa ("{END_MESSAGE}" para sair) -> ')
            if message.lower().strip() == END_MESSAGE:
                break

            client_socket.sendto(message.encode(), (hostname, server_socket_port))

            data, _ = client_socket.recvfrom(1024)
            present_received_from_server(data.decode())


# Utility functions -----------------------------------------------------------
def present_received_from_server(data):
    print(f'Recebido do servidor {data}')
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    client()
