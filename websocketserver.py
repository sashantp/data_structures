import socket
import select
from base64 import b64encode
from hashlib import sha1
from struct import *
import binascii

HOST = 'localhost'
PORT = 8125;
data = ""

SOCKET_LIST = []
CLIENT_LIST = []

def calculate_response_key(key):
    GUID = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    hash = sha1(key.encode() + GUID.encode())
    response_key = b64encode(hash.digest()).strip()
    return response_key.decode('ASCII')


def parse_headers (data):
	headers = {}
	lines = data.splitlines()
	for l in lines:
		parts = l.split(": ", 1)
		if len(parts) == 2:
			headers[parts[0]] = parts[1]
	headers['code'] = lines[len(lines) - 1]
	return headers


def DecodedWebsockRecieve(stringStreamIn):
    byteArray =  stringStreamIn 
    datalength = int(byteArray[1]) & 127
    indexFirstMask = 2 
    if datalength == 126:
        indexFirstMask = 4
    elif datalength == 127:
        indexFirstMask = 10
    masks = [m for m in byteArray[indexFirstMask : indexFirstMask+4]]
    indexFirstDataByte = indexFirstMask + 4
    decodedChars = []
    i = indexFirstDataByte
    j = 0
    while i < len(byteArray):
        decodedChars.append( chr(byteArray[i] ^ masks[j % 4]) )
        i += 1
        j += 1
    return ''.join(decodedChars)

def EncodeWebSockSend(socket,data):
    bytesFormatted = []
    bytesFormatted.append(129)

    bytesRaw = data.encode()
    bytesLength = len(bytesRaw)
    if bytesLength <= 125 :
        bytesFormatted.append(bytesLength)
    elif bytesLength >= 126 and bytesLength <= 65535 :
        bytesFormatted.append(126)
        bytesFormatted.append( ( bytesLength >> 8 ) & 255 )
        bytesFormatted.append( bytesLength & 255 )
    else :
        bytesFormatted.append( 127 )
        bytesFormatted.append( ( bytesLength >> 56 ) & 255 )
        bytesFormatted.append( ( bytesLength >> 48 ) & 255 )
        bytesFormatted.append( ( bytesLength >> 40 ) & 255 )
        bytesFormatted.append( ( bytesLength >> 32 ) & 255 )
        bytesFormatted.append( ( bytesLength >> 24 ) & 255 )
        bytesFormatted.append( ( bytesLength >> 16 ) & 255 )
        bytesFormatted.append( ( bytesLength >>  8 ) & 255 )
        bytesFormatted.append( bytesLength & 255 )

    bytesFormatted = bytes(bytesFormatted)
    bytesFormatted = bytesFormatted + bytesRaw
    socket.send(bytesFormatted) 	

try:

	print "Chat server started on port " + str(PORT)

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server.bind((HOST,PORT))

	server.listen(10)

	conn , addr = server.accept()

	print "Connected " , addr

	# conn.send("HTTP/1.1 101 Switching Protocols\r\n"+
	# 			"Upgrade: WebSocket\r\n"+
	# 			"Connection: Upgrade\r\n"+
	# 			"WebSocket-Origin: \r\n" +
	# 			"WebSocket-Location: ws://"+HOST+":"+str(PORT)+"\r\n"+
	# 			"Sec-WebSocket-Accept: dGhlIHNhbXBsZSBub25jZQ==\r\n\r\n"+
	# 			"Access-Control-Allow-Headers: content-type\r\n")

	data = conn.recv(4096)
	print data
	headers = parse_headers(data)

	print headers['Sec-WebSocket-Key']
	print headers['code']

	response_key_val = calculate_response_key(headers['Sec-WebSocket-Key'])
	print response_key_val

	conn.send("HTTP/1.1 101 Web Socket Protocol Handshake\r\n"+
				"Upgrade: WebSocket\r\n"+
				"Connection: Upgrade\r\n"+
 				"WebSocket-Origin: "+headers['Origin']+"\r\n"+
            	"WebSocket-Location: ws://"+HOST+":"+str(PORT)+"\r\n"+
            	"Access-Control-Allow-Origin: http://sphp"+"\r\n"+
				"Access-Control-Allow-Credentials: true"+"\r\n"+
            	"Sec-WebSocket-Accept: "+str(response_key_val)+"\r\n\r\n")

	while True :
		
		data = conn.recv(1024)
		
		if data :
			print " data "+binascii.b2a_qp(data,True,True,True)
			temp = binascii.b2a_qp(data,True,True,True)
			print temp.decode('utf-8')
			print " data hex "+binascii.b2a_hqx(data)
			print " data from bin "+binascii.b2a_uu(data)
			# print " data decoded " + DecodedWebsockRecieve(data)
			conn.send("hii")

		else :
			conn.close()

	conn.close()		

except socket.error as msg:
	print " Error " , msg




