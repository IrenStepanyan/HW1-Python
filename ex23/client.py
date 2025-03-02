import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 33333))
print("Connecting...")

while True:
	client_message  = input("Client: ")
	client_socket.send(client_message.encode())

	if client_message.lower() == 'exit':
		print("Disconnected.")
		break

	server_message = client_socket.recv(1024).decode()
	print(f"Server: {server_message} ")

client_socket.close()	
