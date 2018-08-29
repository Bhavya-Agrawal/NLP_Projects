#!/usr/bin/python3

import tweepy
from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
import string
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

#writing data into a file to avoid again and again using Tweeter API to avoid blocking
#f = open("/home/bhavyaagrawal/Desktop/tweets.txt",'w+')

# consumer credentials
consumer_key = 'SR426hYSxHVJ98h5hqGMe1TSs'
consumer_secret = '3MS7oWSvxNwJQQzOylHORZiWA94w1bbb1rZSxRKqJ1RRoxuOzh'

#access credentials for tweet access
access_token_key = '831362319850598405-NUKjq8iAXACrvrfS37GMM7tU51UNTDw'
access_token_secret = 'r62sGSSK0yMANUboZSEQ856sOXFa90XQXcpJLvIBNyKgk'

# to authenticate ourself
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

#print(dir(auth))
# to access using acces_token_key and access_token_secret
auth.set_access_token(access_token_key,access_token_secret)


# to access API of tweeter
connect = tweepy.API(auth)

# to search about a particular tweet
analyse = connect.search('Sunny Leone')
# the return type of analyse data is <class 'tweepy.models.SearchResults'> and so to take only text part out of it we are using analyse.text
#print(analyse)

data = []
for tweet in analyse:
	#tweet is actually individual tweet from tweeter
	tweets = tweet.text
	print(tweets)
	#f.write(tweet.text)

	#analysis = TextBlob(tweets)
	# the above statement returns TextBlob type object and so we can apply sentiment over it

	# removing any punctuation from tweet
	tweets_without_punc = [i for i in tweets if i  not in string.punctuation]

	# joining the tweet again into a string
	clean_tweets = ''.join(tweets_without_punc)
	# now taking complete data from the list
	token = word_tokenize(clean_tweets)

	# now removing unwanted words from tweet
	token_clean = [i for i in token if i not in stopwords.words('english')]

	
	# fetching all the analysed_data in a form of string from token list
	analysed_data = ' '.join(token_clean)
	print(analysed_data)

	#print(analysed_data)
	
	'''# to get frequency of each word
	freq_data = nltk.FreqDist(analysed_data)
	freq_data.plot()'''

	# to get polarity we need to make it TextBlob type
	fetched_data = TextBlob(analysed_data)
	#fetched_data = TextBlob(tweets)
	print(fetched_data.sentiment.polarity)

	if fetched_data.sentiment.polarity == 0:
		data.append('neutral')

	elif fetched_data.sentiment.polarity <= 0:
		data.append('negative')

	elif fetched_data.sentiment.polarity >= 0:
		data.append('positive')


print(data)

# now counting total no of polarity 
total = len(data)
neutral_data = data.count('neutral')
negative_data = data.count('negative')
positive_data = data.count('positive')	

# getting the percentage of all data
perc_neutral = (neutral_data/total)*100
perc_negative = (negative_data/total)*100
perc_positive = (positive_data/total)*100	

print(perc_neutral)
print(perc_negative)
print(perc_positive)

plt.bar(['neutral','negative','positive'],[neutral_data,negative_data,positive_data],color=['r','g','b'])
#plt.bar(['neutral','negative','positive'],[perc_neutral,perc_negative,perc_positive],color=['r','g','b'])
plt.show()			

