# Import database connection
from backend.database import conn, cursor


# ---------------- SIGNUP FUNCTION ----------------

def signup_user(username, email, password):

    try:

        # Insert user into database
        cursor.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, password)
        )

        conn.commit()

        return True

    except:

        # Email already exists
        return False


# ---------------- LOGIN FUNCTION ----------------

def login_user(email, password):

    # Find matching user
    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ? AND password = ?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    return user