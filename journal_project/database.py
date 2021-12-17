import sqlite3

connection = sqlite3.connect("journal.db")

# If we want to return the result as a row instead of a default tuple
# connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
            connection.execute(
            "INSERT INTO entries VALUES(?,?)", # Do this to avoid sqlinjections
            (entry_content, entry_date)
            )


def get_entries():
    cursor = connection.execute("SELECT * FROM entries")
    return(cursor)
