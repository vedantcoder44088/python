import socket
import threading

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(5)
print("Server is listening")

# Function to handle messages from the client
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message: {data}")
        response = input("Enter your response: ")
        client_socket.send(response.encode())
    client_socket.close()

# Accept incoming connections
while True:
    client, addr = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client, addr))
    client_handler.start()
