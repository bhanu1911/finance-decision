import cgi
import json
import re
import sys
# import MySQLdb

# debug
import pprint
import cgitb

cgitb.enable()

import config


class Decision(object):
    def __init__(self):
        self.status = 0
        self.output_vars = {'status': config.status_description[0]}
        self.input_vars = {}
        self.request = ''

    def output(self):
        print '\n'.join(config.http_headers)
        print(json.dumps(self.output_vars))

    def check(self):
        pass

    def read(self):
        self.request = json.load(sys.stdin)
        self.request = '{"first_name": "Ivan", "surname": "Rodger", "country": "United Kingdom", "account": 2434523452352354, "address": "Vicarage Hill", "age": 30}'

class DecisionMethods(object):
    def __init__(self, value):
        self.x = value

    def not_eq(self, y):
        if y != self.x:
            return 0

    def not_lt(self, y):
        if y > self.x:
            return 0

    def not_le(self, y):
        if y <= self.x:
            return 0

    def not_gt(self, y):
        if y < self.x:
            return 0

    def not_ge(self, y):
        if y <= self.x:
            return 0


class InputVars(object):
    def __init__(self, **kwargs):
        self.__dict__.update(locals())
        del self.self


class DecisionRules(DecisionMethods):
    def __init__(self):
        pass

    def rules(self, ):
        pass


class NumberRules(object):
    def __init__(self):
        pass


class TextRules(object):
    def __init__(self):
        pass


class DbRules(object):
    def __init__(self):
        pass


class Db:
    def __init__(self, db_type='mysql', host='127.0.0.1', port=3306, database='test', username='root', password=''):
        self.__dict__.update(locals())
        del self.self


class DbMysql:
    def __init__(self, host='127.0.0.1', port=3306, database='test', username='root', password=''):
        pass

    def connect(self):
        pass

    def query(self):
        pass

    def modify_query(self):
        pass

    def select_query(self):
        pass

    def disconnect(self):
        pass

    def __del__(self):
        self.disconnect()