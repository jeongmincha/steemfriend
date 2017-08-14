import json
import urllib.request
import requests

BASE_URL = 'https://steemd.steemit.com/'


def post_database_api(style, params):
    import requests
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
    payload = json.dumps({'method': 'call',
           'params': ['database_api', style, params],
           'id': 0})

    text = requests.post(BASE_URL, data=payload, headers=headers).text
    return json.loads(text)


def get_num_account_history(account):
    hist = post_database_api('get_account_history', [account, -1, 0])
    return int(hist['result'][0][0]) + 1


def get_account_history(account, fr, limit):
    history = post_database_api('get_account_history', [account, fr, limit])
    return history['result']


def get_active_votes(author, permlink):
    active_votes = post_database_api('get_active_votes', [author, permlink])
    return active_votes['result']


def get_content_replies(author, permlink):
    replies = post_database_api('get_content_replies', [author, permlink])
    return replies['result']


def get_all_account_history(account):
    history = []
    num_hist = get_num_account_history(account)
    quotient = num_hist // 1000
    remainder = num_hist % 1000

    history.extend(get_account_history(account, remainder, remainder))
    for i in range(1, quotient+1):
        history.extend(get_account_history(account, remainder + i * 1000, 999))

    return history


def get_permlinks(account):
    history = get_all_account_history(account)
    permlink_set = []

    for i in range(len(history)):
        obj = history[i]
        objtype = obj[1]['op'][0]
        body = obj[1]['op'][1]

        if objtype == "comment" and body['parent_author'] == "":
            permlink_set.append(body['permlink'])

    return set(permlink_set)


def get_vote_counter(account, permlinks=None):
    from collections import Counter
    vote_counter = []
    if permlinks == None:
        permlinks = get_permlinks(account)

    for permlink in permlinks:
        votes = get_active_votes(account, permlink)

        for vote in votes:
            vote_counter.append(vote['voter'])

    vote_counter = Counter(vote_counter)
    return vote_counter


def get_reply_counter(account, permlinks=None):
    from collections import Counter
    reply_counter = []
    if permlinks == None:
        permlinks = get_permlinks(account)

    for permlink in permlinks:
        replies = get_content_replies(account, permlink)

        for reply in replies:
            reply_counter.append(reply['author'])

    reply_counter = Counter(reply_counter)
    return reply_counter


def get_best_friend_list(account):
    print ('get_best_friend_list()')
    permlinks = get_permlinks(account)
    # print ('permlinks: ' + permlinks)
    vote_counter = get_vote_counter(account, permlinks)
    reply_counter = get_reply_counter(account, permlinks)

    from collections import Counter
    friend_factor = Counter()
    for k in vote_counter.keys():
        friend_factor[k] += vote_counter[k] * 0.5
    for k in reply_counter.keys():
        friend_factor[k] += reply_counter[k] * 1

    print (friend_factor)
    return friend_factor.most_common()[1:]
