import sqlite3

# Connect to an in-memory DB (disappears when connection closes)
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE notebook (id INTEGER PRIMARY KEY, name TEXT, description TEXT)")