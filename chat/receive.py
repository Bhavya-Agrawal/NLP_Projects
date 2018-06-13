#!/usr/bin/python3
import time
import socket
#import _thread

rec = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rec.bind(("127.0.0.1",9999))

while True:	
	# msg from sender
	data = rec.recvfrom(1000)
	#data[0].decode()
	print(data[0].decode())	
	#time.sleep(1)

	# data contains a list of 2 dimension 1st is msg from sender 2nd is tuple of(IP,Socket of sender)
	msg = input("Enter your reply...")
	msg = msg.encode()
	#	msg = msg.encode() reply to sender
	rec.sendto(msg,(data[1]))
	#time.sleep(2)


'''# to start thread of msg
_thread.start_new_thread(rec_msg,())

# to start thread of reply
_thread.start_new_thread(rec_reply,())

# to make thread continue
while True:
	pass'''

