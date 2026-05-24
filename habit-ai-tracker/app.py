import streamlit as st

import warnings

warnings.filterwarnings("ignore")
# Database functions
from backend.database import (
    create_table,
    add_habit,
    get_habits
)

# Habit services
from backend.habits_service import (
    complete_habit,
    delete_habit
)

# AI model
from ml.model import predict_habit

# Auth functions
from auth.auth_service import (
    signup_user,
    login_user
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Habit Tracker AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------- LOAD CSS ----------------

with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- CREATE DATABASE ----------------

create_table()

# ---------------- SESSION STATE ----------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "username" not in st.session_state:

    st.session_state.username = ""

# ======================================================
# LOGIN / SIGNUP PAGE
# ======================================================

if st.session_state.logged_in == False:

    st.title("🧠 Habit Tracker AI")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Signup"]
    )

    # ---------------- LOGIN ----------------

    if menu == "Login":

        st.subheader("🔐 Login")

        email = st.text_input("Enter Email")

        password = st.text_input(
            "Enter Password",
            type="password"
        )

        if st.button("Login"):

            user = login_user(email, password)

            # Successful login
            if user:

                st.session_state.logged_in = True

                st.session_state.username = user[1]

                st.success("Login successful!")

                st.rerun()

            else:

                st.error("Invalid email or password")

    # ---------------- SIGNUP ----------------

    elif menu == "Signup":

        st.subheader("📝 Signup")

        username = st.text_input("Enter Username")

        email = st.text_input("Enter Email")

        password = st.text_input(
            "Enter Password",
            type="password"
        )

        if st.button("Create Account"):

            success = signup_user(
                username,
                email,
                password
            )

            if success:

                st.success(
                    "Account created successfully!"
                )

            else:

                st.error(
                    "Email already exists"
                )

# ======================================================
# MAIN APP
# ======================================================

else:

    # ---------------- TITLE ----------------

    st.markdown(
        f"""
        <p class="dashboard-title">
        🧠 Welcome {st.session_state.username}
        </p>
        """,
        unsafe_allow_html=True
    )

    # ---------------- SIDEBAR ----------------

    menu = st.sidebar.selectbox(
        "Navigation",
        ["Dashboard", "Add Habit", "Analytics"]
    )

    # Logout button
    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.username = ""

        st.rerun()

    # ======================================================
    # DASHBOARD
    # ======================================================

    if menu == "Dashboard":

        st.subheader("📊 Your Habits")

        habits = get_habits()

        if len(habits) == 0:

            st.warning("No habits added yet")

        else:

            for habit in habits:

                prediction, confidence = predict_habit(
                    habit[2],
                    str(int(habit[2]) + 2)
                )

                st.markdown(
                    f'''
                    <div class="habit-card">

                        <div class="habit-title">
                            ✅ {habit[1]}
                        </div>

                        <br>

                        <div class="streak-text">
                            🔥 Streak: {habit[2]} Days
                        </div>

                        <br>

                        <div class="ai-text">
                            🤖 AI Success Score:
                            {confidence}%
                        </div>

                    </div>
                    ''',
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                # Complete Button
                with col1:

                    if st.button(
                        f"Complete {habit[0]}"
                    ):

                        complete_habit(habit[0])

                        st.rerun()

                # Delete Button
                with col2:

                    if st.button(
                        f"Delete {habit[0]}"
                    ):

                        delete_habit(habit[0])

                        st.rerun()

    # ======================================================
    # ADD HABIT
    # ======================================================

    elif menu == "Add Habit":

        st.subheader("➕ Add New Habit")

        habit_name = st.text_input(
            "Enter Habit Name"
        )

        if st.button("Save Habit"):

            if habit_name == "":

                st.error(
                    "Please enter habit name"
                )

            else:

                add_habit(habit_name)

                st.success(
                    f"{habit_name} added successfully!"
                )

    # ======================================================
    # ANALYTICS
    # ======================================================

    elif menu == "Analytics":

        st.subheader("📈 Analytics")

        habits = get_habits()

        total_habits = len(habits)

        total_streak = 0

        for habit in habits:

            total_streak += int(habit[2])

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f'''
                <div class="analytics-box">
                    <h2>📋 Total Habits</h2>
                    <h1>{total_habits}</h1>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f'''
                <div class="analytics-box">
                    <h2>🔥 Total Streak</h2>
                    <h1>{total_streak}</h1>
                </div>
                ''',
                unsafe_allow_html=True
            )

        st.info(
            "More AI analytics coming soon 🚀"
        )