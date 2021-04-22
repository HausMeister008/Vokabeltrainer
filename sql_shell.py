import sqlite3 as sql
import os

con = sql.connect("vokabeln.db")

cur = con.cursor()

print('STARTING SQL SHELL')

while True:
    line = input('>>> ')
    if line == '':
        continue
    else:
        query = line
        if sql.complete_statement(query):
            try:
                query = query.strip()
                cur.execute(query)

                if query.lstrip().upper().startswith('SELECT'):
                    print(cur.fetchall())
                else:
                    print('SUCCESS')
            except sql.Error as e:
                print('AN ERROR OCCURED:', e.args[0])