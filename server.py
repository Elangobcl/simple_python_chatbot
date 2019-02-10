import socket 
from threading import Thread
import sys

server = socket.socket()
port_num = 2000
server.bind(("", port_num)) # "" listens to all clients in a network if  127.0.0.1 has passed listens only to the calls made within the local computer
server.listen(100) #listen to n num of clients
conn,addr = server.accept() #conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection

clients = {}
name = conn.recv(1000)
clients[name] = conn

print ("{0} and {1}" .format(conn, addr))

def receive_data():
	while True:
		try:
			data = conn.recv(1000)
			print("client : %s"% data.decode())
		except KeyboardInterrupt:
			server.close()
	   		break
def send_data():
	while True:
		try:
			server_input = raw_input()
			conn.sendall(server_input.encode())
		except KeyboardInterrupt:
			server.close()
	   		break
		

if __name__ == "__main__":
  
	try:
		t= Thread(target= receive_data)
		t.start()
		send_data()
	except KeyboardInterrupt:
		server.close()
		sys.exit()

