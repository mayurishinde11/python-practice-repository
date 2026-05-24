import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Analytics Function
def show_analytics(habits):

    st.subheader("📈 Habit Analytics")

    # Check if habits exist
    if len(habits) == 0:

        st.warning("No habits available")

    else:

        # Store data for chart
        habit_names = []
        streaks = []

        # Loop through habits
        for habit in habits:

            habit_names.append(habit[1])

            streaks.append(habit[2])

        # Create dataframe
        df = pd.DataFrame({
            "Habit": habit_names,
            "Streak": streaks
        })

        # Show table
        st.dataframe(df)

        # Create chart
        fig, ax = plt.subplots()

        ax.bar(
            habit_names,
            streaks
        )

        # Labels
        ax.set_xlabel("Habits")

        ax.set_ylabel("Streak Days")

        ax.set_title("Habit Streak Progress")

        # Show chart
        st.pyplot(fig)