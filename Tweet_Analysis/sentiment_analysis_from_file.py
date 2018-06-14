#!/usr/bin/python3
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize

f = open("/home/bhavyaagrawal/Desktop/tweets.txt","r+")

# data redaing from file
data = f.read()
print("data @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ")
print(data)

#clening the data by first tockenizing then removing stopwords

# tokenize data as per words
token_data = word_tokenize(data)


# now remove unwanted or extra words from tockenized data
fresh_data = [i for i in token_data if i not in stopwords.words('english')]
#print(type(fresh_data))  its return type is list 

# plotting graph using top 20 most frequent words
freq_data = nltk.FreqDist(fresh_data)
freq_data.plot(20)

#print(fresh_data)
#fresh data is in form of list to convert it again into string

clean_data = ' '.join(fresh_data)
print("clean_data ###################################################################")
print(clean_data)

# sentimental analysis on the data 
for i in fresh_data:
	analysing_data = TextBlob(i)
	sentiments = analysing_data.sentiment
	print(sentiments)
	print(type(sentiments))	
	if sentiments.polarity == 0:
		print("feelings are neutral")

	elif sentiments.polarity < 0:
		print("feelings are negative")

	elif sentiments.polarity > 0:
		print("feelings are positive")

	else:
		print("sentiments are not obtained correctly")	
	
