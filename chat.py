import socket
import select

HOST = ''
PORT = 8125
data = ""

SOCKET_LIST = []
CLIENT_TO_SOCKET_MAP = {}
IP_PORT_TO_USER_MAP = {}

try:

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((HOST,PORT))
	server.listen(10)

	SOCKET_LIST.append(server)
	
	print "Chat server started on port " + str(PORT)

	while True :
		# print CLIENT_TO_SOCKET_MAP
		# print IP_PORT_TO_USER_MAP
		ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST, [],[])

		for sock in ready_to_read :

			if sock == server : # new connection request , get username 
				conn , addr = server.accept()
				username = conn.recv(4096)

				if len(username) > 0 and username not in CLIENT_TO_SOCKET_MAP :
				
					SOCKET_LIST.append(conn)
					CLIENT_TO_SOCKET_MAP[username] = conn
					peername,port = conn.getpeername()
					ip_port = peername+"_"+str(port)
					IP_PORT_TO_USER_MAP[ip_port] = username
					print " Connected : " , username
					conn.send("success")
				
				else:
					conn.send("User already present , please choose another name ")
					conn.close()
					continue

			else: # added client
				
				try:

					data = sock.recv(1024)
					peername,port = sock.getpeername()
					ip_port = peername+"_"+str(port)
					print "user " , IP_PORT_TO_USER_MAP[ip_port] , " " , data
					
					if len(data) > 0 :
					
						for user,current_socket in CLIENT_TO_SOCKET_MAP.iteritems() :
							if current_socket != server and current_socket == sock :
								try:
									current_socket.send("this is server message")
								except socket.error as msg:
									current_socket.close()
									if user in CLIENT_TO_SOCKET_MAP :
										del CLIENT_TO_SOCKET_MAP[user]
										SOCKET_LIST.remove(current_socket)
									print " current_socket ",msg
					else:
					
						SOCKET_LIST.remove(sock)
						del CLIENT_TO_SOCKET_MAP[IP_PORT_TO_USER_MAP[ip_port]]
						del IP_PORT_TO_USER_MAP[ip_port]
						sock.close()
				
				except socket.error as msg:	
				
					SOCKET_LIST.remove(sock)
					del CLIENT_TO_SOCKET_MAP[IP_PORT_TO_USER_MAP[ip_port]]
					del IP_PORT_TO_USER_MAP[ip_port]
					sock.close()
					print "offline"
					print " Error receiving " , msg
					continue
					
	server.close()
					
except socket.error as msg:
	print " Error outer " , msg
