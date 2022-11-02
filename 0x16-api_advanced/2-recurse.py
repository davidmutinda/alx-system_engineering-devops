#!/usr/bin/python3
"""
This module queries reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list containing titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-agent": "Linux-david"}
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    results = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')
    for c in results.get('children'):
        hot_list.append(c.get('data').get('title'))

    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after, count)
