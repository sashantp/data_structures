import socket
import select

HOST = ''
PORT = 8125;
data = ""

SOCKET_LIST = []
CLIENT_LIST = []

try:

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server.bind((HOST,PORT))

	server.listen(5)

	# peername = server.getpeername()
	# print peername[1]

	SOCKET_LIST.append(server)
	
	print "Chat server started on port " + str(PORT)

	while True :

		conn , addr = server.accept()

		print "client connected " , addr

		print server.getsockname()

		print conn.fileno()
		print conn.getsockname()
		print conn.getpeername()

		peername = conn.getpeername()
		print peername[1]

		if peername[1] in CLIENT_LIST :
			try:
				data = conn.recv(1024)
				print "chat" , data
				if data :
					for current_socket in SOCKET_LIST:
						if current_socket != server and current_socket == conn :
							current_socket.send("this is server message")
				else:
					conn.close()
			except socket.error as msg:	
				print "offline"
				print " Error " , msg
				conn.close()
		else :
			CLIENT_LIST.append(peername[1])
			print " Connected : " , addr
					

		print CLIENT_LIST


# 	while True :

# 		ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST, [],[])

# 		print "ready_to_read" ,ready_to_read

# 		for sock in ready_to_read :

# 			if sock == server : # new connection request
# 				conn , addr = server.accept()
# 				SOCKET_LIST.append(conn)
# 				print " Connected : " , addr

# 			else:
# 				try:
# 					data = sock.recv(1024)
# 					print "chat" , data
# 					if data :
# 						for current_socket in SOCKET_LIST:
# 							if current_socket != server and current_socket == sock :
# 								current_socket.send("this is server message")
# 					else:
# 						sock.close()
# 				except socket.error as msg:	
# 					print "offline"
# 					print " Error " , msg
# 					sock.close()


except socket.error as msg:
	print " Error " , msg


# def chat_server():
	
# 	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 	server.bind((HOST,PORT))

# 	server.listen(5)

# 	SOCKET_LIST.append(server)

# 	print 'Chat server started at ' + str(port)

# 	while True:

# 		ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [] , [] , 0)

# 		for connection in ready_to_read :

# 			if connection == server : # new connection

# 				conn , addr = server.accept()

# 				SOCKET_LIST.append(conn)

# 				print " New client connected at " + addr

# 				broadcast(server,)

# 			# else :
			






# # broadcast 
# def broadcast(socket_server,sock,message):
	
# 	for socket in SOCKET_LIST :
# 		if sock != socket_server and sock != socket :
# 			try :
# 				socket.send(message)
# 			except :
# 				socket.close()
# 				if socket in SOCKET_LIST :
# 					SOCKET_LIST.remove(socket)