import socket


def server():
    hostname = socket.gethostname()
    port = 8000

    server_socket = socket.socket()
    server_socket.bind(tuple([hostname, port]))

    # how many clients the server can listen simultaneously
    server_socket.listen(1)

    print(f'Ouvindo na porta {port}...')
    connection_socket, address = server_socket.accept()

    print(f'Conexão de {address}')

    while True:
        data_packet = connection_socket.recv(1024).decode()
        if not data_packet:
            break

        print(f'Recebido do usuário conectado: {data_packet}')
        
        # send data uppercase to the client
        connection_socket.send(data_packet.upper().encode())
    connection_socket.close()


if __name__ == '__main__':
    server()
