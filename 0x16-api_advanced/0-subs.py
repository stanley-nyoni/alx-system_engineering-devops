#!/usr/bin/python3
""" Module for a function that queries the Reddit API and returns the
number of subscribers for a given subreddit. """


import requests


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit. """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/Max)'
    }
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 404:
        return 0

    return response.json().get('data').get('subscribers')
