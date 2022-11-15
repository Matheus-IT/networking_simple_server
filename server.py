import socket


def server():
    """This is the main function for the server"""

    hostname = socket.gethostname()
    port = 8000

    implementation_choices = {
        '1': use_tcp_socket_implementation,
        '2': use_udp_socket_implementation,
    }

    choice = input('Qual implementação deseja usar? (1-TCP | 2-UDP) -> ')

    use_chosen_socket_implementation = implementation_choices[choice]

    use_chosen_socket_implementation(hostname, port)


# socket implementations to choose from ---------------------------------------
def use_tcp_socket_implementation(hostname, port):
    instantiate_tcp_socket = lambda: socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )

    with instantiate_tcp_socket() as server_socket:
        server_socket.bind(tuple([hostname, port]))

        server_socket.listen(1) # how many clients the server can listen

        present_listening_on(port)

        connection_socket, _ = server_socket.accept()

        while True:
            data_packet = connection_socket.recv(1024).decode()
            if not data_packet:
                break
            connection_socket.send(data_packet.upper().encode())

def use_udp_socket_implementation(hostname, port):
    instantiate_udp_socket = lambda: socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM,
    )

    with instantiate_udp_socket() as server_socket:
        server_socket.bind(tuple([hostname, port]))

        present_listening_on(port)

        while True:
            data_packet, address = server_socket.recvfrom(1024)
            if not data_packet:
                break
            data_packet = data_packet.decode().upper()
            server_socket.sendto(data_packet.encode(), address)


# Utility functions -----------------------------------------------------------
def present_listening_on(port):
    print(f'Ouvindo na porta {port}...')
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    server()
