#!/usr/bin/python3
"""
This module queries reddit API
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-agent": "Linux-david"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    array = response.json().get('data').get('children')
    for count, el in enumerate(array):
        if count == 10:
            break
        print(el.get('data').get('title'))
