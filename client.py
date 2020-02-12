from socket import *
server_name = 'localhost'
server_port = 12000

# Create socket
client_socket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
# Send to the server
client_socket.sendto(message.encode(), (server_name, server_port))

# Receiver response back
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())

# Close the socket
client_socket.close()
