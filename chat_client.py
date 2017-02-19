import socket

HOST = ''
PORT = 8125
data = ""

try :

	client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	client.connect((HOST,PORT))

	while 1 :

		user_input = raw_input("Please type message or Enter to close :")
	 	if len(user_input) == 0 : 
	 		client.close()
	 		break
		if len(user_input) > 0 :
			client.send(user_input)
			data = client.recv(1024)
			print "chat" , data

	client.close()

	print 'Received' , repr(data)

except socket.error as msg:

	print 'Error' , msg	