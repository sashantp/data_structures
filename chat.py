import socket
import select

HOST = ''
PORT = 8125
data = ""

SOCKET_LIST = []
CLIENT_LIST = []

try:

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((HOST,PORT))
	server.listen(10)

	SOCKET_LIST.append(server)
	
	print "Chat server started on port " + str(PORT)

	while True :

		ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST, [],[])

		print "ready_to_read" ,ready_to_read

		for sock in ready_to_read :

			if sock == server : # new connection request
				conn , addr = server.accept()
				SOCKET_LIST.append(conn)
				print " Connected : " , addr

			else:
				try:
					data = sock.recv(1024)
					print "chat" , data
					if len(data) > 0 :
						print SOCKET_LIST
						for current_socket in SOCKET_LIST:
							if current_socket != server and current_socket == sock :
								try:
									current_socket.send("this is server message")
								except socket.error as msg:
									current_socket.close()
									SOCKET_LIST.remove(current_socket)
									print "current_socket ",msg
					else:
						SOCKET_LIST.remove(sock)
						sock.close()
				except socket.error as msg:	
					SOCKET_LIST.remove(sock)
					sock.close()
					print "offline"
					print " Error while" , msg
					continue
					
	server.close()				
except socket.error as msg:
	print " Error outer " , msg
