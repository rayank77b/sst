import sqlite3, os
import MySQLdb

class cSqlite:
    ''' cSqlite is a simple wrapper class for sqlite3 
        
        db = cSqlite('mydatabase.db')
        db.write("CREATE ....")           # do a commit
        db.read("SELECT ...")             # return a row back
    '''
    def __init__(self, file='/tmp/sqlite3stresstest.db'):
        self.filename=file
        # remove the file if exists!
        try:
            os.remove(file)
        except:
            pass
        self.conn = sqlite3.connect(file)

    def create(self, sql):
        sql = sql%''
        self.write(sql)

    def write(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        c.close()

    def read(self, sql):
        c = self.conn.cursor()
        row = c.execute(sql).fetchall()
        c.close()
        return row


class NoReadError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class cDevNull:
    ''' cDevNull is a simple wrapper class for /dev/null calls
        
        db = cDevNull()
        db.write("CREATE ....")           # do a commit
        db.read("SELECT ...")             # should return an exception
    '''
    def __init__(self, file='/dev/null'):
        self.filename=file
        self.fd = open(file, 'w')

    def create(self, sql):
        sql = sql%''
        self.write(sql)

    def write(self, sql):
        self.fd.write(sql)

    def read(self, sql):
        #raise NoReadError("cDevNull can't call read()")
        pass

class cMySQL:
    ''' cMySQL is a simple wrapper class for MySQL
        user and password should be in the sqlconfig.py configuration
        
        db = cMySQL(sqlconfig)
        db.write("CREATE ....")           # do a commit
        db.read("SELECT ...")             # return a row back
        
    '''
    def __init__(self, sqlc):
        self.sqlc = sqlc
        self.username = sqlc['user']
        self.password = sqlc['password']
        self.db = sqlc['dbname']
        self.conn = MySQLdb.connect(host="localhost", db="mysql", user=self.username, passwd=self.password)
        try:
            self.write("DROP DATABASE IF EXISTS %s"%self.db)
        except:
            pass
        self.write("CREATE DATABASE %s"%self.db)
        self.write("USE %s"%self.db)

    def create(self, sql):
        sql = sql%self.sqlc['autokey']
        self.write(sql)

    def write(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        c.close()

    def read(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        row = c.fetchall()
        c.close()
        return row
