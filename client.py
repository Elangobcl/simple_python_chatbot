import socket 
from threading import Thread
import sys

client = socket.socket()
port_num = 2000
# connect to the server on local computer
client.connect(("localhost", port_num))

def receive_data():
	while True:
	    try:
		data = client.recv(1000)
		print("Server : %s"% data.decode())
	    except KeyboardInterrupt:
		client.close()
	   	break
def send_data():
	while True:
	  try:
		client_input = raw_input()
		client.sendall(client_input.encode())
	  except KeyboardInterrupt:
		client.close()
	   	break
if __name__ == "__main__":
   try:
	t= Thread(target= receive_data)
	t.start()
	send_data()
   except KeyboardInterrupt:
	client.close()
	sys.exit()
	
