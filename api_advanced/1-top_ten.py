#!/usr/bin/python3
"""
defines the main function to get
the top tem hot titles from the reddit
api
"""
import requests
import sys

"""
    main function for the subcriber count
"""
def top_ten(subreddit):
    #  main moadule
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    try:
        response = requests.get(api_url, allow_redirects=False)
        data = response.json()
        return data['data']['children']['data'][4]['title']
    except requests.exceptions.RequestException as e:
        print(e)
        return 0
