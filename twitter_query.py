'''
    twitter_query.py
    
    This file contains useful utility functions. In the real world,
    we would have no such file because functions should be contained
    in files or directories that they are used in.
'''

from dotenv import load_dotenv
import tweepy
import random
import os
from os.path import join, dirname

KEY_CONTENTS = "contents"
KEY_DATE = "date"
KEY_AUTHOR = "author"
KEY_URL = "url"

dotenv_path = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_path)

TWITTER_ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
TWITTER_KEY = os.environ['KEY']
TWITTER_KEY_SECRET = os.environ['KEY_SECRET']

def auth(access_token, access_token_secret, key, key_secret):
    auth = tweepy.OAuthHandler(key, key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def get_relevant_tweets(query, access_token, access_token_secret, key, key_secret, count = 10):
    api = auth(access_token, access_token_secret, key, key_secret)
    results = api.search(q=query, count = count)
    relevant_tweets = []
    for result in results:
        contents = result.text
        author = "@" + result.author.screen_name
        url = result.source_url
        date = result.created_at
        
        relevant_tweets.append({
            KEY_CONTENTS: contents, 
            KEY_DATE: date.strftime("%m/%d/%Y, %H:%M"), 
            KEY_AUTHOR: author, 
            KEY_URL: url,
        })
        
    return relevant_tweets
    
def get_random_tweet(tweets):
    return random.choice(tweets)
