import socket 
from threading import Thread
import sys
import sqlite3

server = socket.socket()
port_num = 2000
server.bind(("", port_num))
server.listen(100) #listen to n num of clients

connection = sqlite3.connect('chat.db')
c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS client (name VARCHAR(20), email VARCHAR(20), addr VARCHAR(20));""")

clients = {}


def receive_data(cli_name, cli_conn, cli_addr):
	while True:
		try:
			c.execute("""select * from client where name = {};""".format(cli_name))
			result = c.fetchall()
			data = cli_conn.recv(1000)
			msg = cli_name +":"+" " +data.decode() 	
			for client in clients:
				if(cli_name!=client):
					clients[client].sendall(msg.encode())
		except KeyboardInterrupt:
			server.close()
	   		break
		

if __name__ == "__main__":
  while True:
	
	try:
		conn,addr = server.accept()
		print (" connected to {0} and {1}" .format(conn, addr))

		cli_info = conn.recv(1000)
		cli_info = cli_info.decode()
		cli_list = cli_info.split(',')
		name = cli_list[1]		
		email = cli_list[2]
		clients[name] = conn
		query = """INSERT INTO client (name, email, addr) values ("{0}", "{1}", "{2}");""".format(name, email, addr[0])
		print("Got connection from client at address {0} and name {1}" .format(addr, name))		
		c.execute(query)
		connection.commit()
		c.execute("""select * from client;""")
		result = c.fetchall()
		print result
		t= Thread(target= receive_data, args = (name, conn, addr))
		t.start()
	except KeyboardInterrupt:
		server.close()
		sys.exit()

