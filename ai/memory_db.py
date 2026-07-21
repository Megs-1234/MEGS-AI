from database.database import cursor, connection


def save_message(user_id, role, message):

    cursor.execute(
        """
        INSERT INTO memory
        (user_id, role, message)

        VALUES (?, ?, ?)
        """,

        (user_id, role, message)
    )

    connection.commit()


def load_messages(user_id):

    cursor.execute(
        """
        SELECT role, message

        FROM memory

        WHERE user_id=?

        ORDER BY id ASC
        """,

        (user_id,)
    )

    rows = cursor.fetchall()

    messages = []

    messages.append(
        {
            "role":"system",
            "content":
            "You are MEGS AI. Reply naturally. Do not use Markdown."
        }
    )

    for role, message in rows:

        messages.append(

            {
                "role":role,
                "content":message
            }

        )

    return messages