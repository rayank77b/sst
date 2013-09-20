import getrandom

# the sql structur is the main configuration structur of sst.py
sql = { 

'debug':0,
'debugsql':0,

'tables':('user','address'),

'address':{'create':'CREATE TABLE address (id INTEGER PRIMARY KEY %s, street TEXT, nr INTEGER, zipcode INTEGER, town TEXT, state TEXT);',
           'insert':"INSERT INTO address (street, nr, zipcode, town, state) VALUES ('%s', '%d', '%d', '%s', '%s');",
           'call':(getrandom.street, getrandom.street_nr, getrandom.zipcode, getrandom.town, getrandom.state),
           'select':'SELECT * FROM address LIMIT %d;',
           'cnt':1000,
        },
'user':{'create':'CREATE TABLE user (id INTEGER PRIMARY KEY %s, name TEXT, gender VARCHAR(50), age INTEGER, zeit DATE, address INTEGER);',
        'insert':"INSERT INTO user (name,gender,age,zeit, address) VALUES ('%s','%s','%d','%s', '%d');",  
        'call':(getrandom.name, getrandom.gender, getrandom.age, getrandom.date, getrandom.address),
        'select':'SELECT * FROM user LIMIT %d;',
        'cnt':10000,
        },


'join':'SELECT * FROM user INNER JOIN address ON user.address=address.id LIMIT %d;',

'mysql':{'user':'root', 'password':'mysql456', 'dbname':'sqlitestresstest', 'autokey':'NOT NULL AUTO_INCREMENT'}
}
