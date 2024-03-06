from socket import *
import threading

SERVER_PORT = 1200
SERVER_HOST = "127.0.0.1"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_HOST, SERVER_PORT))

name = input("Enter your name: ")

def listen_for_messages():
    while True:
        message = clientSocket.recv(1024).decode()
        print("\n" + message)

t = threading.Thread(target=listen_for_messages)
t.daemon = True 
t.start()

print("Enter your message ('q' to quit): ")

while True:
    message = input()
    if message == 'q':
        break
    message = f'{name}: {message}'
    clientSocket.send(message.encode())

clientSocket.close()
