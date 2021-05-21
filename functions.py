import sqlite3
con = sqlite3.connect("vokabeln.db")

class SQL():
    def __init__(self):
        self.cur = con.cursor()

    def insert(self, front, back, addition = '',fach = 'englisch'):
        print('\nINSERTING')

        self.cur.execute('INSERT INTO vokabeln (vorderseite, rueckseite, zusatz, subject) values(?, ?, ?, ?)', (front, back, addition, fach))
        con.commit()


    def delete(self, id):
        print('\nDELETING - ID:' +  str(id))

        if isinstance(id, int):
            self.cur.execute(f'delete from vokabeln where id = {id}')

        elif isinstance(id, list):
            to_delete = ','.join(str(id) for id in id)
            self.cur.execute(f'delete from vokabeln where id in {to_delete}')
        con.commit()


    def get(self, id = 0, order = 'desc', ordered_by = 'id'):
        print('\nGETTING CONTENT')

        if order.lower() not in ['asc', 'desc']:
            order = 'desc'

        if ordered_by.lower() not in ['level', 'id', 'lvl']:
            ordered_by = 'id'
        if ordered_by.lower() == 'lvl':
            ordered_by = 'level'

        return_value = []

        if id != 0:
            if str(id).isdigit():
                for row in self.cur.execute(f'select * from vokabeln where id = {id} order by {ordered_by} {order}'):
                    return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3], 'lvl': row[4], 'fach': row[5]})

            elif isinstance(id, list):
                search_for = ','.join([str(id) for id in id])
                for row in self.cur.execute(f'select * from vokabeln where id in ( {search_for} ) order by {ordered_by} {order}'):
                    return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3], 'lvl': row[4], 'fach': row[5]})

        else:
            for row in self.cur.execute(f'select * from vokabeln order by {ordered_by} {order}'):
                return_value.append({'id': row[0], 'front': row[1], 'back': row[2], 'add': row[3], 'lvl': row[4], 'fach': row[5]})

        return return_value
    
    def update(self, vokabel_id, aufstieg:int):
        print('\nUPDATING')
        query = f"UPDATE vokabeln SET level = level + {aufstieg}  WHERE id = {vokabel_id}"
        self.cur.execute(query)
        con.commit()


# ---- USAGE ----

if __name__ == '__main__':
    sql = SQL()

    # print(sql.get())
    # sql.delete(5)
    # sql.insert('The meaning of life', 'Der Sinn des Lebens', 'The meaning of life is not so obvious for many people. But the ones who found it are probably not as happy about it as they thought...')
    # print(sql.get(id = [1,2],order='desc'))

    # sql.update(5, 8)


# content = sql.get()
# for i in content:
#     print('ID:',i['id'], '\n   Front:', i['front'], '\n   Back:', i['back'], '\n   Addition:', i['add'])

# sql.delete(content[-1][0])