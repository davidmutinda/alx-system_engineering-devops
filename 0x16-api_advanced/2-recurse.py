#!/usr/bin/python3
"""
This module queries reddit API
"""
import requests


def recurse(subreddit, hot_list=[], count=0):
    """
    Returns a list containing titles of all hot articles for a given subreddit
    """
    if not hot_list:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {"User-agent": "Linux-david"}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None
        subreddit = response.json().get('data').get('children')
        # print(response.json().get('data').get('children')[1].get('data').get('id'))
        hot_list.append(subreddit[count].get('data').get('title'))
        return recurse(subreddit, hot_list, count + 1)
    if count >= len(subreddit):
        # print(hot_list)
        return hot_list
    else:
        hot_list.append(subreddit[count].get('data').get('title'))
        return recurse(subreddit, hot_list, count + 1)
