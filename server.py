from socket import *
server_port = 12000

# Create a socket (UDP)
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind to port
server_socket.bind(('', server_port))

# Now listen
print('The server is ready to receive message...')
while True:
    # Receive message
    message, client_address = server_socket.recvfrom(2048)
    print("Got the message: " + message.decode())
    modified_message = message.decode().upper()
    # Send it back
    server_socket.sendto(modified_message.encode(), client_address)
