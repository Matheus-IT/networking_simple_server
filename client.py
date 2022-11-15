import socket


def client_program():
    hostname = socket.gethostname()
    socket_server_port = 8000

    client_socket = socket.socket()
    
    # connecting to the server
    client_socket.connect((hostname, socket_server_port))

    END_MESSAGE = 'tchau'

    while True:
        message = input(f'Digite alguma coisa ("{END_MESSAGE}" para sair) -> ')
        if message.lower().strip() == END_MESSAGE:
            break

        # send message uppercase back to the server
        client_socket.send(message.encode())

        # receive response from server
        data = client_socket.recv(1024).decode()

        print(f'Recebido do servidor {data}')

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
