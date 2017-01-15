import socket

HOST = ''
PORT = 8125;


try:

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	s.bind((HOST,PORT))

	s.listen(1)

	conn , addr = s.accept()

	print " Connected : " , addr

	while 1 :
		data = conn.recv(1024)
		print "chat" , data
		if not data : break
		conn.sendall(data)

	conn.close()

except socket.error as msg:
	print " Error " , msg