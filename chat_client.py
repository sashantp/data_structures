import socket

HOST = '127.0.0.4'
PORT = 8125
data = ""

try :

	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	s.connect((HOST,PORT))

	while 1 :

		user_input = raw_input("Please type message or Enter to close :")
	 	if len(user_input) == 0 : break
		if len(user_input) > 0 :
			s.sendall(user_input)
			data = s.recv(1024)
			print "chat" , data

	s.close()

	print 'Received' , repr(data)

except socket.error as msg:

	print 'Error' , msg	