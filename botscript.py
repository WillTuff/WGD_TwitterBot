import tweepy
import csv
import random

from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

with open ('list.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    yourList= map(tuple, reader)

randomLink = random.choice(yourList)

fullUrl = (''.join(randomLink))

api.update_status(fullUrl)
