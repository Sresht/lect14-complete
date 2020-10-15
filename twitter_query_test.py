'''
    twitter_query_test.py
    
    This file tests twitter_query.py.
'''

import unittest
from twitter_query import get_relevant_tweets, get_random_tweet
from twitter_query import KEY_CONTENTS, KEY_DATE, KEY_AUTHOR, KEY_URL
from twitter_query import DATABASE_URL, TWITTER_ACCESS_TOKEN, \
            TWITTER_ACCESS_TOKEN_SECRET, TWITTER_KEY, TWITTER_KEY_SECRET

import unittest.mock as mock
from dotenv import load_dotenv
import tweepy
import random
import os
from os.path import join, dirname


KEY_INPUT = "input"
KEY_EXPECTED = "expected"

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
dotenv_path = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_path)

class TwitterQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "Biggie Smalls",
                KEY_EXPECTED: {
                    KEY_AUTHOR: "@triciascot99",
                    KEY_DATE: "10/15/2020, 21:24",
                    KEY_URL: "http://twitter.com/download/iphone",
                }
            },
        ]

    def mocked_random_choice(self, values):
        return values[0]


    def test_get_random_tweet_success(self):
        for test_case in self.success_test_params:
            relevant_tweets = get_relevant_tweets(
                query = test_case[KEY_INPUT],
                access_token = TWITTER_ACCESS_TOKEN,
                access_token_secret = TWITTER_ACCESS_TOKEN_SECRET,
                key = TWITTER_KEY,
                key_secret = TWITTER_KEY_SECRET,
                count = 3)
                
            with mock.patch('random.choice', self.mocked_random_choice):
                random_tweet = get_random_tweet(relevant_tweets)
                
            expected = test_case[KEY_EXPECTED]
            
            self.assertEqual(random_tweet[KEY_AUTHOR], expected[KEY_AUTHOR])
            self.assertEqual(random_tweet[KEY_DATE], expected[KEY_DATE])
        
if __name__ == '__main__':
    unittest.main()
