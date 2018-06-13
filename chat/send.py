#!/usr/bin/python3
import time
import socket
#import _thread

send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(True):
	
		msg = input("Enter the msg...")
		msg = msg.encode()
	
		# msg to receiver
		send.sendto(msg,("127.0.0.1",9999))
		#time.sleep(1)

		#reply from receiver
		reply = send.recvfrom(1000)
		print(reply[0].decode())
		#time.sleep(2)






# try to use Thread in future
''''def sender_send():
	while(True):
	
		msg = input("Enter the msg...")
		msg = msg.encode()
	
		# msg to receiver
		send.sendto(msg,("127.0.0.1",9999))
		#time.sleep(1)
	
def sender_reply():	
	while True:	
		#reply from receiver
		reply = send.recvfrom(1000)
		print(reply[0].decode())
		#time.sleep(2)


# start thread of sending
_thread.start_new_thread(sender_send,())


# start thread of receiving
_thread.start_new_thread(sender_reply,())


# to make thread to continue
while True:
	pass'''

