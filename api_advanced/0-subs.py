#!/usr/bin/python3
"""Query Reddit API and return the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit, or 0 if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (custom reddit api script)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
