from socket import *
import threading

SERVER_PORT = 1200
SERVER_HOST = "127.0.0.1"

s = socket(AF_INET, SOCK_STREAM)
client_sockets = []

def listen_for_client(clientsocket, address):
    print(f"Connection from {address} has been established!")
    while True:
        try:
            text = clientsocket.recv(1024).decode("utf-8")
            if not text:
                print(f"Connection with {address} has been closed by the client.")
                break
            elif text == "q":
                print(f"Connection with {address} has been terminated by the client.")
                break
            print(f"{address}: {text}")
            broadcast(text)
        except ConnectionResetError:
            print(f"Connection with {address} has been reset.")
            break
    clientsocket.close()

def broadcast(message):
    for client_socket in client_sockets:
        client_socket.send(message.encode())

def start():
    try:
        s.bind((SERVER_HOST, SERVER_PORT))
        print("Server is ready to receive")
        s.listen(5)
        while True:
            clientsocket, address = s.accept()
            client_sockets.append(clientsocket)  # Add client socket to the list
            thread = threading.Thread(target=listen_for_client, args=(clientsocket, address))
            thread.start()
    except OSError as e:
        print(f"Error: {e}")
    finally:
        s.close()

start()
