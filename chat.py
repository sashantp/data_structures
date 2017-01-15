import socket

HOST = ''
PORT = 8125;
data = ""

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
		user_input = raw_input("Please type message: or Enter to close")
		conn.sendall(user_input)
		if len(user_input) == 0 : break

	conn.close()

except socket.error as msg:
	print " Error " , msg