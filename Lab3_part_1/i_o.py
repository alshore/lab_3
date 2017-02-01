import sqlite3


def setup():

    juggler_list = []

    try:
        db = sqlite3.connect('chainsaw_jugglers.db')
        cur = db.cursor()
        cur.execute('drop table if exists chainsaw')
        cur.execute('create table chainsaw (name text, country text, catches int)')

    except sqlite3.Error:
        print('error creating table')

    finally:
        db.close()

    try:
        db = sqlite3.connect('chainsaw_jugglers.db')
        cur = db.cursor()

        with db:
            cur.execute('insert into chainsaw values ("Ian Stewart", "Canada", 94)')
            cur.execute('insert into chainsaw values ("Aaron Gregg", "Canada", 88)')
            cur.execute('insert into chainsaw values ("Chad Taylor", "USA", 78)')


    except sqlite3.Error as e:
        print('Error adding rows')
        print(e)

    finally:
        db.close()

    try:
        db = sqlite3.connect('chainsaw_jugglers.db')
        cur = db.cursor()

        for row in cur.execute('select * from chainsaw'):
            juggler_list = [row]

    except sqlite3.Error as e:
        print('Error selecting data from chainsaw table')
        print(e)

    finally:
        db.close()

    return juggler_list


def shutdown():

    try:
        db = sqlite3.connect('chainsaw_jugglers.db')
        cur = db.cursor()
        with db:
            cur.execute('drop table chainsaw')

    except sqlite3.Error as e:
        print('Error deleting chainsaw table')
        print(e)
    finally:
        db.close()

