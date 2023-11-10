#!/usr/bin/python3
'''Defines recursive function to
return hot posts in a subreddit
'''
import requests


def recurse(subreddit, hot_list=[], fullname=None, count=0):
    '''fetches all hot posts in a subreddit
    with a recursive function

    Return:
        None - if subreddit is invalid
    '''
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': fullname, 'limit': 100, 'count': count}
    headers = {'user-agent': 'glenmirale18'}
    info = requests.get(url, headers=headers,
                        params=params, allow_redirects=False)
    if (info.status_code % 400) < 100:
        return None
    info_json = info.json()
    results = info_json.get('data').get('children')
    new_packet = [post.get('data').get('title') for post in results]
    hot_list += new_packet
    after = info_json.get('data').get('after', None)
    dist = info_json.get('data').get('dist')
    count += dist
    if after:
        recurse(subreddit, hot_list, after, count)
    return hot_list
