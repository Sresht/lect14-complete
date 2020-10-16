'''
    twitter_query_test.py
    
    This file tests twitter_query.py.
'''

import unittest
from twitter_query import get_relevant_tweets, get_random_tweet
from twitter_query import KEY_CONTENTS, KEY_DATE, KEY_AUTHOR, KEY_URL
from twitter_query import TWITTER_ACCESS_TOKEN, \
            TWITTER_ACCESS_TOKEN_SECRET, TWITTER_KEY, TWITTER_KEY_SECRET

import unittest.mock as mock
from dotenv import load_dotenv
import tweepy
import os
import datetime
from os.path import join, dirname

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class MockedAuthorResponse:
    def __init__(self, screen_name):
        self.screen_name = screen_name

class MockedSearchResponse:
    def __init__(self, text, screen_name, source_url, created_at):
        self.text = text
        self.author = MockedAuthorResponse(screen_name)
        self.source_url = source_url
        self.created_at = created_at

class TwitterQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "Biggie Smalls",
                KEY_EXPECTED: {
                    KEY_CONTENTS: "mocked tweet",
                    KEY_AUTHOR: "@triciascot99",
                    KEY_DATE: "10/15/2020, 21:24",
                    KEY_URL: "http://twitter.com/download/iphone",
                }
            },
        ]
        
    def mocked_random_choice(self, values):
        return values[0]
    
    def mocked_api_search(self, q, count):
        return [
            MockedSearchResponse(
                "mocked tweet",
                "triciascot99",
                "http://twitter.com/download/iphone",
                datetime.datetime.strptime("10/15/2020, 21:24", "%m/%d/%Y, %H:%M")),
            MockedSearchResponse(
                "aslfdjasdf",
                "sadfasdfas",
                "asfjkaldfjad",
                datetime.datetime.strptime("10/19/2020, 21:01", "%m/%d/%Y, %H:%M")),
            ]

    def test_get_random_tweet_success(self):
        for test_case in self.success_test_params:
            with mock.patch('tweepy.API.search', self.mocked_api_search):
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
            
            self.assertDictEqual(random_tweet, expected)
        
if __name__ == '__main__':
    unittest.main()
