import socket
import threading

SERVER = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            client_socket.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()
    while True:
        message = input("")
        try:
            client.send(message.encode('utf-8'))
        except:
            client.close()
            break

if __name__ == "__main__":
    main()
