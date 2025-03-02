import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 33333))
server_socket.listen(1)
print("Connecting... ")

client_socket, client_add = server_socket.accept()
print("Connected")

while True:
	client_message = client_socket.recv(1024).decode()
	if client_message.lower() == 'exit':
		print("Disconnected")
		break
	print(f"Client: {client_message} ")

	server_message = input("Server: ")
	client_socket.send(server_message.encode())

client_socket.close()
server_socket.close()


