#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for unsuccessful responses

        data = response.json().get('data')
        if data:
            subscriber_count = data.get('subscribers')
            return subscriber_count if subscriber_count is not None else 0
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return 0

# Example usage:
subreddit_name = 'python'
subscribers = number_of_subscribers(subreddit_name)
print(f"The number of subscribers in r/{subreddit_name} is: {subscribers}")

