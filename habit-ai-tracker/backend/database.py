import os
import sqlite3

# Create data folder automatically
os.makedirs("data", exist_ok=True)

# Connect SQLite database
conn = sqlite3.connect(
    "data/habits.db",
    check_same_thread=False
)

cursor = conn.cursor()


# Function to create habits table
# Function to create tables
def create_table():

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Habits table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        streak INTEGER DEFAULT 0
    )
    """)

    conn.commit()

# Function to add new habit
def add_habit(title):

    cursor.execute(
        "INSERT INTO habits (title) VALUES (?)",
        (title,)
    )

    conn.commit()


# Function to get all habits
def get_habits():

    cursor.execute("SELECT * FROM habits")

    return cursor.fetchall()