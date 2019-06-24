import sqlite3


class Database:
    # Initialize the object of the class. The constructor
    def __init__(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name text, manufacturer text, serial text, year integer)")
        conn.commit()
        conn.close()

    # Insert function
    def insert(self, name, manufacturer, serial, year):
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        # Null value will autoincrement the primary key
        cur.execute("INSERT INTO item VALUES (NULL,?,?,?,?)", (name, manufacturer, serial, year))
        conn.commit()
        conn.close()

    # View function
    def view(self):
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM item ")
        rows = cur.fetchall()
        # Does not require commit method
        conn.close()
        return rows

    # Search function
    # Initialize the parameters with a default empty value to avoid error of no arguments passed
    def search(self, name="", manufacturer="", serial="", year=""):
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM item WHERE name=? OR manufacturer=? OR serial=? OR year=?",
                    (name, manufacturer, serial, year))
        rows = cur.fetchall()
        conn.close()
        return rows

    # Delete function
    def delete(self, id):
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        # Remember to include the last comma
        cur.execute("DELETE FROM item WHERE id=?", (id,))
        conn.commit()
        conn.close()

    # Update function
    def update(self, id, name, manufacturer, serial, year):
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("UPDATE item SET name=?, manufacturer=?, serial=?, year=? WHERE id=?",
                    (name, manufacturer, serial, year, id))
        conn.commit()
        conn.close()

# Call the connect function so that it can always execute on the frontend script
# insert('Laptop', 'Dell', '00500', 2008)
# delete(2)
# print(search(manufacturer="Japan"))
# update(4, 'Laptop', 'Mac', '00300', 2009)
# print(view())
