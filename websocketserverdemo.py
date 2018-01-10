# from websocket import create_connection
# import websocket
# import thread
# import time

# def on_message(ws,message):
# 	print message


# def on_close():
# 	print "closed"

# def on_error(es,error):
# 	print error

# def on_open(ws):
# 	ws.send("hello")
# 	ws.close()


# ws = websocket.webSocket()

# ws.connect("ws://localhost:8125")


# if __name__ == '__main__':
# 	websocket.enableTrace(True)
# 	ws = websocket.WebSocketApp("ws://localhost:8125", 
# 		on_message = on_message, 
# 		on_error = on_error, 
# 		on_close= on_close)

# 	ws.on_open = on_open


# ws = create_connection("ws://localhost:8125")
# print "Sending 'Hello, World'..."
# ws.send("Hello, World")
# print "Sent"
# print "Receiving..."
# result =  ws.recv()
# print "Received '%s'" % result
# ws.close()



import asyncio
import websockets

@asyncio.coroutine
def hello(websocket, path):
	name = await websocket.recv()
	print("< {}".format(name))

	greeting = "Hello {}!".format(name)
	await websocket.send(greeting)
	print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8125)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()