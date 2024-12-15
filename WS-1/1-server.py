import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = []

def handle_client(client_socket, address):
    clients.append(client_socket)
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast_message(message, client_socket)
    finally:
        clients.remove(client_socket)
        client_socket.close()

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                pass

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    main()
