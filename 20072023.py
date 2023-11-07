import socket

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# Function to send and receive messages
def send_receive():
    while True:
        message = input("Enter your message: ")
        client.send(message.encode())
        response = client.recv(1024).decode()
        print(f"Received from server: {response}")

# Run the send and receive loop
send_receive()
