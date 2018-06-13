#!/usr/bin/python3
import time
import socket
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize,word_tokenize

send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(True):

		msg = input("Can u please tell me the meaning with example of my msg...")
		msg = msg.encode()
	
		# msg to receiver
		send.sendto(msg,("127.0.0.1",9999))
		#time.sleep(1)

		#reply from receiver
		print("thankyou so much my friend ,now let me tell u the meaning of ur query......")
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		reply = send.recvfrom(1000)
		#print(reply[0].decode())

		# to show meaning of reply to receiver
		rec_data = reply[0].decode()

		'''# data after being tokenized or listed
		rec_data = word_tokenize(rec_data)

		# making the list out of rec_data
		rec = [rec_data for i in rec_data]'''

		# printing names of books having the meaning of rec_data
		#print(wordnet.synsets(rec_data))
		books = wordnet.synsets(rec_data)
		#books = wordnet.synsets(rec)

		# printing defintion  and example as per book 1
		definition = books[0].definition()
		example = books[0].examples()

		print("the definition of the ur reply as per me is!!    ")
		print(definition)

		print("for example!!    ")
		print(example)


		#time.sleep(2)







