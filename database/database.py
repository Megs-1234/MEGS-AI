import sqlite3

connection = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER,

role TEXT,

message TEXT

)
""")

connection.commit()

def clear_memory(user_id):

    cursor.execute(
        """
        DELETE FROM memory
        WHERE user_id=?
        """,
        (user_id,)
    )

    connection.commit()
