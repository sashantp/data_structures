import socket
import select

HOST = 'localhost'
PORT = 8125;
data = ""

SOCKET_LIST = []
CLIENT_LIST = []

try:

	print "Chat server started on port " + str(PORT)

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server.bind((HOST,PORT))

	server.listen(10)

	conn , addr = server.accept()

	print "Connected " , addr

	conn.send("HTTP/1.1 101 Web Socket Protocol Handshake\r\n"
				+"Upgrade: WebSocket\r\n"
				+"Connection: Upgrade\r\n")

 			"WebSocket-Origin: \r\n" .
            "WebSocket-Location: ws://"+HOST+":"+PORT+"\r\n".
            "Sec-WebSocket-Accept: ""\r\n\r\n";

	# data = conn.recv(4096)
	# print data 

	while True :
		
		data = conn.recv(4096)
		
		if data :
			print data
			conn.send("this is server message")
		else :
			conn.close()

	conn.close()		

except socket.error as msg:
	print " Error " , msg
