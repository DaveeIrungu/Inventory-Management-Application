import sqlite3


# create and connect to db
def connect():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, item_name text, item_manufacturer text, item_serial text, item_year integer)")
    conn.commit()
    conn.close()

# Call the connect function so that it can always execute on the frontend script
connect()
