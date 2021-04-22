import sqlite3 as sql

con = sql.connect("vokabeln.db")
cur = con.cursor()

def insert( front, back, addition):
    print('INSERTING')
    cur.execute('INSERT INTO vokabeln (vorderseite, rueckseite, zusatz) values(?, ?, ?)', (front, back, addition))
    con.commit()
    for row in cur.execute('select * from vokabeln'):
        print(row)
