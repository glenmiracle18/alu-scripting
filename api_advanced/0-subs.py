#!/usr/bin/python3
# this is a test file for the reddit api
import requests
import sys

"""
    main function for the subcriber count
"""
def subscribers_count(subreddit):
    #  main moadule
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(api_url, allow_redirects=False)
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(e)
        return 0


if __name__ == "__main__":
    subreddit = sys.argv[1]
    if len(sys.argv) < 2:
        print('please parse an argument')
    else:
        subcribers = subscribers_count(subreddit)
        print(subcribers)
