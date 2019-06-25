import sqlite3


class Database:
    # Initialize the object of the class. The constructor
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name text, manufacturer text, serial text, year integer)")
        self.conn.commit()

    # Insert function
    def insert(self, name, manufacturer, serial, year):
        # Null value will autoincrement the primary key
        self.cur.execute("INSERT INTO item VALUES (NULL,?,?,?,?)", (name, manufacturer, serial, year))
        self.conn.commit()

    # View function
    def view(self):
        self.cur.execute("SELECT * FROM item ")
        rows = self.cur.fetchall()
        # Does not require commit method
        return rows

    # Search function
    # Initialize the parameters with a default empty value to avoid error of no arguments passed
    def search(self, name="", manufacturer="", serial="", year=""):
        self.cur.execute("SELECT * FROM item WHERE name=? OR manufacturer=? OR serial=? OR year=?",
                         (name, manufacturer, serial, year))
        rows = self.cur.fetchall()
        return rows

    # Delete function
    def delete(self, id):
        # Remember to include the last comma
        self.cur.execute("DELETE FROM item WHERE id=?", (id,))
        self.conn.commit()

    # Update function
    def update(self, id, name, manufacturer, serial, year):
        self.cur.execute("UPDATE item SET name=?, manufacturer=?, serial=?, year=? WHERE id=?",
                         (name, manufacturer, serial, year, id))
        self.conn.commit()

    # Function for closing db connection
    def __del__(self):
        self.conn.close()

# Call the connect function so that it can always execute on the frontend script
# insert('Laptop', 'Dell', '00500', 2008)
# delete(2)
# print(search(manufacturer="Japan"))
# update(4, 'Laptop', 'Mac', '00300', 2009)
# print(view())
