import pymssql
import json
from collections import Counter


def calculate_vote_counter(account, active_votes):
    vote_counter = []
    for idx in range(len(active_votes)):
        votes = json.loads(active_votes[idx][2])
        for vote in votes:
            vote_counter.append(vote['voter'])

    vote_counter = Counter(vote_counter)
    return vote_counter.most_common()


def get_best_friends(account):
    cursor = SteemSQLCursor()
    vote_counter = calculate_vote_counter(account, cursor.get_active_votes(account))
    reply_counter = cursor.get_reply_counter(account)

    friend_counter = Counter()
    for vote in vote_counter:
        friend_counter[vote[0]] += vote[1] * 0.5
    for reply in reply_counter:
        friend_counter[reply[0]] += reply[1] * 1

    friend_counter = friend_counter.most_common()
    remove_idx = -1
    for idx, friend in enumerate(friend_counter):
        if friend[0] == account:
            remove_idx = idx
    if remove_idx != -1:
        del friend_counter[remove_idx]

    return friend_counter


class SteemSQLCursor:
    def __init__(self):
        self.conn = pymssql.connect(host='sql.steemsql.com', \
            user='steemit', \
            password='steemit', \
            database='DBSteem')
        self.cursor = None


    def select_sql_with_account(self, fn, account):
        self.cursor = self.conn.cursor()
        reply_counter = []

        with open(fn, 'r') as f:
            lines = f.readlines()
            lines[0] = lines[0][:-1] + "'" + str(account) + "'\n"

            sql = str()
            for line in lines:
                sql += line
            # print (sql)
            # sql = f.read()

            self.cursor.execute(sql)
            for row in self.cursor:
                reply_counter.append(row)
            self.cursor.close()

        return reply_counter


    def get_active_votes(self, account):
        return self.select_sql_with_account("./friend/data_handling/active_votes.sql", account)


    def get_reply_counter(self, account):
        return self.select_sql_with_account("./friend/data_handling/reply_counter.sql", account)
