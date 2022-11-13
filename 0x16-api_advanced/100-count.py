#!/usr/bin/python3
"""Count the occurences of word in title"""
import requests


def count_words(subreddit, word_list, after='', count={}):
    """Check the how recurring a list of words are in subreddit title"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after != '':
        url += '?after={}'.format(after)
    user = {'User-Agent': 'Test123'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if not response.ok or response.status_code == 302:
        return None
    data = response.json().get('data')
    after = data.get('after')
    for post in data.get('children'):
        for word in post.get('data').get('title').casefold().split():
            for keyword in word_list:
                if keyword.casefold() == word:
                    if keyword.casefold() not in count.keys():
                        count[word] = 1
                    else:
                        count[word] += 1
    if after is None:
        sorted_count = dict(sorted(count.items(),
                                   key=lambda x: (-x[1], x[0])))
        for k, v in sorted_count.items():
            if v > 0:
                print('{}: {}'.format(k, v))
        return
    count_words(subreddit, word_list, after, count)
