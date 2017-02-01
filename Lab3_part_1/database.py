import sqlite3

db = sqlite3.connect('chainsaw_jugglers.db')

cur = db.cursor() 
cur.execute('drop table if exists chainsaw')
cur.execute('create table chainsaw (record holder, country, number of catches)')


cur.execute('insert into chainsaw values ("Ian Stewart", "Canada", 94)')
cur.execute('insert into chainsaw values ("Aaron Gregg", "Canada", 88)')
cur.execute('insert into chainsaw values ("Chad Taylor", "USA", 78)')

db.commit()


for row in cur.execute('select * from chainsaw'):
    print(row)

cur.execute('drop table chainsaw')

db.commit()

db.close()