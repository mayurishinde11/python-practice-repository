# Import database connection
from backend.database import conn, cursor


# Function to increase streak
def complete_habit(habit_id):

    # Get current streak
    cursor.execute(
        "SELECT streak FROM habits WHERE id = ?",
        (habit_id,)
    )

    result = cursor.fetchone()

    # Check if habit exists
    if result:

        current_streak = result[0]

        # Increase streak
        new_streak = current_streak + 1

        # Update database
        cursor.execute(
            "UPDATE habits SET streak = ? WHERE id = ?",
            (new_streak, habit_id)
        )

        conn.commit()


# Function to delete habit
def delete_habit(habit_id):

    cursor.execute(
        "DELETE FROM habits WHERE id = ?",
        (habit_id,)
    )

    conn.commit()