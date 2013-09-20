import sqlconfig

def generate_insert(db, table, sql):
    cnt = sql[table]['cnt']
    for d in range(cnt):
        werte=[]
        for x in range(0, len(sql[table]['call'])):
            werte.append(sql[table]['call'][x]())
        #print sql[table]['insert']%tuple(werte)
        db.write(sql[table]['insert']%tuple(werte))

def generate_read(db, table, sql, limit):
    debug=cnt = sql['debugsql']
    row=db.read(sql[table]['select']%limit)
    if debug==1:
        print row

def generate_join(db, sql, limit):
    debug=cnt = sql['debugsql']
    row=db.read(sql['join']%limit)
    if debug==1:
        print row
