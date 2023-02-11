import socket
import threading

name = input("Choose a nick name : ")
target = '127.0.0.1'
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target,port))

def recieve():
	while True:
		try:
			message = client.recv(1024).decode("ascii")
			if message == "NAME ":
				client.send(name.encode("ascii"))
			else:
				print(message)
		except:
			print("Error occurred!")
			client.close()
			break
def write():
	while True:
		message = f'{name}: {input("")}'
		client.send(message.encode("ascii"))
r_thread = threading.Thread(target=recieve)
r_thread.start()

w_thread = threading.Thread(target=write)
w_thread.start()
