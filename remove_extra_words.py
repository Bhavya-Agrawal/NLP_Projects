#!/usr/bin/python3

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
import string

# take user input
keyword = input("Enter the text!! \n")

# tockenize or split the keyword as per the words
token = word_tokenize(keyword)

# remove unwanted words from the input
# operation on the list 
for i in token:
	if i in stopwords.words('english'):
		token.remove(i)

#print("The filtered text is ",token)

# converting list token again to a valid sentence but join values with a space in between so do ' '.join() else ''.join()
sentence = ' '.join(token)
print(sentence)


# remove punctuation marks from the input
y = [i for i in keyword if i not in string.punctuation]
# the above line will compare each character of keyword with the punctuations present in string module of nltk
print(y)

# making string from y again
valid = ''.join(y)
print(valid)