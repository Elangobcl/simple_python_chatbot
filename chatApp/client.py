import socket 
from threading import Thread
import sys

cliet = socket.socket()
port_num = 2000
# connect to the server on local computer
cliet.connect(("localhost", port_num))

name = raw_input("Enter the name of client: ")
email = raw_input("Enter the name of mailid: ")
cl_id = raw_input("Enter the name of id: ")
msg = "{0}, {1}, {2}" .format(cl_id, name, email)
cliet.sendall(msg.encode())

def receive_data():
	while True:
	    try:
		data = cliet.recv(1000)
		print(data.decode())
	    except KeyboardInterrupt:
		cliet.close()
	   	break
def send_data():
	while True:
	  try:
		cliet_input = raw_input()
		cliet.sendall(cliet_input.encode())
	  except KeyboardInterrupt:
		cliet.close()
	   	break
if __name__ == "__main__":
   try:
	t= Thread(target= receive_data)
	t.start()
	send_data()
   except KeyboardInterrupt:
	cliet.close()
	sys.exit()
