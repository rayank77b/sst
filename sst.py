#!/usr/bin/python
#
# sqlite Stress Test ;)
# test the throughput of sqlite
#
# Andrej Frank, GPL 2.0   2011
# Version 0.01

import sys, getopt, getrandom, time
from functions import *
import dbs
import sqlconfig

'''
    sst - sqlite stress test

    test the throughput of sqlite

    -z  write to /dev/zero, no read possible
    -s  write/read to sqlite database
    -m  write/read to mysql database 
    -c=cnt  create cnt of items
'''

def usage():
    print '''
    sst.py  [option] 

    stress test for sqlite

    -z  write to /dev/zero, no read possible
    -s  write/read to sqlite database
    -m  write/read to mysql database 
'''    

def debug(text):
    global sql
    if sql['debug']==1:
        print "[+] %s"%text

try:                                
    opts, args = getopt.getopt(sys.argv[1:], "hzsm", ) 
except getopt.GetoptError:
    usage()
    sys.exit(2)

if opts==[]:
    usage()
    sys.exit(2)

sql=sqlconfig.sql

for opt, arg in opts:
    if opt == '-z':
        test='devzero'    
        db = dbs.cDevNull()
    elif opt == '-s':
        test='sqlite'
        db = dbs.cSqlite()
    elif opt in ("-m"): 
        test='mysql'
        db = dbs.cMySQL(sql['mysql'])
    else:
        usage()
        sys.exit(2)

debug("start test %s"%test)

start = time.time()
debug("create address")
db.create(sql['address']['create'])
debug("create user")
db.create(sql['user']['create'])
stop = time.time()
print "[+] difference create: %f"%(stop-start)

start = time.time()
debug("insert in address")
generate_insert(db, 'address', sql)
getrandom.set_address_cnt(sql['address']['cnt'])
debug("insert in user")
generate_insert(db, 'user', sql)
stop = time.time()
print "[+] difference insert: %f"%(stop-start)


start = time.time()
debug("read from address")
generate_read(db, 'address', sql, 100)
debug("read from user")
generate_read(db, 'user', sql, 100)
stop = time.time()
print "[+] difference read: %f"%(stop-start)


start = time.time()
debug("join address+user")
generate_join(db, sql, 100)
stop = time.time()
print "[+] difference read: %f"%(stop-start)

