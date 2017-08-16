import pymssql


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
            print (sql)
            # sql = f.read()

            self.cursor.execute(sql)
            for row in self.cursor:
                reply_counter.append(row)
            self.cursor.close()

        return reply_counter


    def get_active_votes(self, account):
        return self.select_sql_with_account("active_votes.sql", account)


    def get_reply_counter(self, account):
        return self.select_sql_with_account("reply_counter.sql", account)
