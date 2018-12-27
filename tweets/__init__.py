#!/usr/bin/python3

from flask import Flask,render_template,request
import tweepy
from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
import string
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def tweet():
    #writing data into a file to avoid again and again using Tweeter API to avoid blocking
    #f = open("/home/bhavyaagrawal/Desktop/tweets.txt",'w+')

    if request.method=='POST':
        words = request.form['t']
        # consumer credentials
        consumer_key = '####################'
        consumer_secret = '########################'

        #access credentials for tweet access
        access_token_key = '############################'
        access_token_secret = '###########################'

        # to authenticate ourself
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

        #print(dir(auth))
        # to access using acces_token_key and access_token_secret
        auth.set_access_token(access_token_key,access_token_secret)


        # to access API of tweeter
        connect = tweepy.API(auth)

        # to search about a particular tweet
        analyse = connect.search(words)
        # the return type of analyse data is <class 'tweepy.models.SearchResults'> and so to take only text part out of it we are using analyse.text
        #print(analyse)

        data = []
        for tweet in analyse:
            #tweet is actually individual tweet from tweeter
            tweets = tweet.text
            print(tweets)
            tweets_without_punc = [i for i in tweets if i  not in string.punctuation]
            clean_tweets = ''.join(tweets_without_punc)
            token = word_tokenize(clean_tweets)
            token_clean = [i for i in token if i not in stopwords.words('english')]
            analysed_data = ' '.join(token_clean)
            print(analysed_data)
            fetched_data = TextBlob(analysed_data)
            print(fetched_data.sentiment.polarity)
            if fetched_data.sentiment.polarity == 0:
                data.append('neutral')
            elif fetched_data.sentiment.polarity <= 0:
                data.append('negative')
            elif fetched_data.sentiment.polarity >= 0:
                data.append('positive')


        print(data)
        total = len(data)
        neutral_data = data.count('neutral')
        negative_data = data.count('negative')
        positive_data = data.count('positive')	

        perc_neutral = (neutral_data/total)*100
        perc_negative = (negative_data/total)*100
        perc_positive = (positive_data/total)*100	

        print(perc_neutral)
        print(perc_negative)
        print(perc_positive)

        plt.bar(['neutral','negative','positive'],[neutral_data,negative_data,positive_data],color=['r','g','b'])
        plt.show()			
    return render_template('tweet.html')


if __name__=="__main__":
    app.run(debug=True)
