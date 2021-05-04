import sqlite3
con = sqlite3.connect("vokabeln.db")

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


    def get(self, id = 0, order = 'asc', ordered_by = 'id'):
        print('\nGETTING CONTENT')

        if order.lower() not in ['asc', 'desc']:
            order = 'asc'

        if ordered_by.lower() not in ['level', 'id', 'lvl']:
            ordered_by = 'id'
        if ordered_by.lower() == 'lvl':
            ordered_by = 'level'

        return_value = []

        if id != 0:
            if str(id).isdigit():
                for row in self.cur.execute(f'select * from vokabeln where id = {id} order by {ordered_by} {order}'):
                    return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3], 'lvl': row[4]})

            elif isinstance(id, list):
                search_for = ','.join([str(id) for id in id])
                for row in self.cur.execute(f'select * from vokabeln where id in ( {search_for} ) order by {ordered_by} {order}'):
                    return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3], 'lvl': row[4]})

        else:
            for row in self.cur.execute(f'select * from vokabeln order by {ordered_by} {order}'):
                return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3], 'lvl': row[4]})

        return return_value
    
    def update(self, vokabel_id, aufstieg:int):
        print('\nUPDATING')
        query = f"UPDATE vokabeln SET level = level + {aufstieg}  WHERE id = {vokabel_id}"
        self.cur.execute(query)
        con.commit()


# ---- USAGE ----

# sql = SQL()


# print(sql.get(id = [1,2],order='desc'))

# sql.update(1, -1)

# sql.insert('appropriate', 'angebracht', 'it seemed appropriate to help her')

# content = sql.get()
# for i in content:
#     print('ID:',i['id'], '\n   Front:', i['front'], '\n   Back:', i['back'], '\n   Addition:', i['add'])

# sql.delete(content[-1][0])