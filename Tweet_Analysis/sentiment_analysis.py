#!/usr/bin/python3

import tweepy
from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

#writing data into a file to avoid again and again using Tweeter API to avoid blocking
f = open("/home/bhavyaagrawal/Desktop/tweets.txt",'w+')
analyse_list = []

# consumer credentials
#consumer_key = '#########'
#consumer_secret = '#######'

#access credentials for tweet access
#access_token_key = '###################'
#access_token_secret = '#################'

# to authenticate ourself
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

#print(dir(auth))
# to access using acces_token_key and access_token_secret
auth.set_access_token(access_token_key,access_token_secret)


# to access API of tweeter
api = tweepy.API(auth)

# to search about a particular data or word in tweet
analyse = api.search('Modi')
print(type(analyse))

# the return type of analyse data is <class 'tweepy.models.SearchResults'> and so to take only text part out of it we are using analyse.text
#print(analyse)

for i in analyse:
	print(i.text)
	f.write(i.text)
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	analysis = TextBlob(i.text)
	# the above statement returns TextBlob type object and so we can apply sentiment over it

	analyse_list.append(analysis)
	# to analyse sentiments from each tweet
	print(analysis.sentiment)


# now taking complete data from the list
token = [i for i in analyse_list]
# to get frequency of each word

freq_data = nltk.FreqDist(token)
freq_data.plot(20)

