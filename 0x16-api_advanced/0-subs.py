#!/usr/bin/python3
''' 0-subs.py '''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers
    '''
    user = {'User-Agent': 'Max'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))

