import MySQLdb


class Db:
    def __init__(self, db_type='mysql', host='127.0.0.1', port=3306, database='test', username='root', password=''):
        self.__dict__.update(locals())
        del self.self
        self.connection = 0
        self.cursor = 0

    def connect(self):
        self.connection = MySQLdb.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                                          db=self.database)
        self.cursor = self.connection.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def __del__(self):
        self.disconnect()
