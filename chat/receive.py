#!/usr/bin/python3
import time
import socket
from nltk.corpus import wordnet

rec = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rec.bind(("127.0.0.1",9999))

while True:	
	print("ya sure,why not my friend.......\n")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	# msg from sender
	data = rec.recvfrom(1000)
	#data[0].decode()
	#print(data[0].decode())	

	# now to print the meaning of the msg obtained using NLP
	decoded_data = data[0].decode()

	# printing the names of books having meaning of the input text
	#print(wordnet.synsets(decoded_data))

	# to print definition of text as per book one alongwith the ans
	books = wordnet.synsets(decoded_data)
	definition = books[0].definition()
	example = books[0].examples()
	print("the meaning of ur input is !!!    ")
	print(definition)
	print("like for example!!    ")
	print(example)


	# data contains a list of 2 dimension 1st is msg from sender 2nd is tuple of(IP,Socket of sender)
	msg = input("Now please can u also do the same for my reply please.....")
	msg = msg.encode()
	#	msg = msg.encode() reply to sender
	rec.sendto(msg,(data[1]))
	#time.sleep(2)



