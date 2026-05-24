import streamlit as st

def show_add_habit():

    st.subheader("➕ Add Habit")

    habit = st.text_input(
        "Enter habit name"
    )

    if st.button("Save Habit"):

        st.success(
            f"{habit} added successfully!"
        )