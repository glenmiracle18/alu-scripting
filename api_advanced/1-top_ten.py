#!/usr/bin/python3
"""
defines the main function to get
the top tem hot titles from the reddit
api
"""
import requests
import sys


def top_ten(subreddit):
    """
    Sends a query to the reddit api to get the hot ten titles
    for a particular subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return (0)
    endpoint = 'https://www.reddit.com'
    headers = {'user-agent': 'Testapi/1.0 by glenmiracle18'}
    params = {'limit': 10}
    info = requests.get('{}/r/{}/hot.json'.format(
        endpoint,
        subreddit), headers=headers, params=params, allow_redirects=False)
    if info.status_code == 200:
        data_info = info.json()
        for post in data_info.get('data').get('children'):
            print(post.get('data').get('title'))
    else:c
        return (0)
