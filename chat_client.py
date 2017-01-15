import socket

HOST = '127.0.0.4'
PORT = 8125

try :

	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	s.connect((HOST,PORT))

	user_input = raw_input("Please type message:")

	if len(user_input) > 0:

		s.sendall(user_input)

		data = s.recv(1024)

	s.close()

	print 'Received' , repr(data)

except socket.error as msg:

	print 'Error' , msg	