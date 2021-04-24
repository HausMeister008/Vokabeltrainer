import sqlite3 as sql
con = sql.connect("vokabeln.db")

class SQL():
    def __init__(self):
        self.cur = con.cursor()


    def insert(self, front, back, addition = ''):
        print('\nINSERTING')

        self.cur.execute('INSERT INTO vokabeln (vorderseite, rueckseite, zusatz) values(?, ?, ?)', (front, back, addition))
        con.commit()


    def delete(self, id):
        print('\nDELETING - ID:' +  str(id))

        if isinstance(id, int):
            self.cur.execute(f'delete from vokabeln where id = {id}')

        elif isinstance(id, list):
            to_delete = ','.join(str(id) for id in id)
            self.cur.execute(f'delete from vokabeln where id in {to_delete}')
        con.commit()


    def get(self, id = 0):
        print('\nGETTING CONTENT')

        return_value = []

        if id != 0:
            if str(id).isdigit():
                for row in self.cur.execute('select * from vokabeln where id = {id}'):
                    return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3]})

            elif isinstance(id, list):
                search_for = ','.join([str(id) for id in id])
                for row in self.cur.execute(f'select * from vokabeln where id in ( {search_for} )'):
                    return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3]})

        else:
            for row in self.cur.execute('select * from vokabeln'):
                return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3]})

        return return_value


# ---- USAGE ----

# sql = SQL()

# sql.insert('appropriate', 'angebracht', 'it seemed appropriate to help her')

# content = sql.get()
# for i in content:
#     print('ID:',i['id'], '\n   Front:', i['front'], '\n   Back:', i['back'], '\n   Addition:', i['add'])

# sql.delete(content[-1][0])