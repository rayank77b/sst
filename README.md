sst
===

sst - simple sqlite stress test script in python.


Why? sst is a simple stress test script to test how fast is sqlite in simple create, insert, select and joins. And to compare sqlite to /dev/zero (fast writing, no reading) and to mysql. The sst sript generate his data randomly.

sst.py - main script to getopt and start the process.
sqlconfig.py - the configuration file, how to create sql request and other configuration stuff, a python structur.
dbs.py - the different class of database calls.
getrandom.py - return different strings to populate the database .
functions.py - help functions.

how to create insert:
write the insert sql request:
'insert':"INSERT INTO address (street, nr, zipcode, town, state) VALUES ('%s', '%d', '%d', '%s', '%s');",
then write a list which functions should be called for the insert fields:
'call':(getrandom.street, getrandom.street_nr, getrandom.zipcode, getrandom.town, getrandom.state),
the call list will be iterated in for loop, append to a list and later insert%list, get joined.

Some results

sqliteStressTest_v0.01$ ./sst.py -s
[+] difference create: 0.005831
[+] difference insert: 55.734122
[+] difference read: 0.002010
[+] difference read: 0.002074

sqliteStressTest_v0.01$ ./sst.py -m
[+] difference create: 0.004647
[+] difference insert: 2.767019
[+] difference read: 0.002793
[+] difference read: 0.002886

sqliteStressTest_v0.01$ ./sst.py -z
[+] difference create: 0.000027
[+] difference insert: 0.432473
[+] difference read: 0.000016
[+] difference read: 0.000007

Here we can see that insert is the most time consumption. And that sqlite need more time as mysql or /dev/zero.
	




