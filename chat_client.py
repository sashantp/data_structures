import socket

HOST = ''
PORT = 8125
data = ""
ack = ""

try :

	client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	client.connect((HOST,PORT))

	user_input = raw_input("Please enter an username :")

	if len(user_input) > 0 :
		client.send(user_input)
		ack = client.recv(4096)
		if len(ack) :
			print ack

	if len(ack) > 0 and ack == "success" :
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