import streamlit as st
import yaml
from passlib.hash import pbkdf2_sha256

# Load user data from YAML file
def load_user_data():
    with open("config.yaml", "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader) or {}

# Save user data to YAML file
def save_user_data(data):
    with open("config.yaml", "w") as file:
        yaml.dump(data, file)

# Register a new user
def register_user(username, password, user_type):
    users = load_user_data()
    if username in users:
        st.warning("User already exists. Please choose another username.")
    else:
        hashed_password = pbkdf2_sha256.hash(password)
        users[username] = {"password": hashed_password, "user_type": user_type}
        save_user_data(users)
        st.success("Registration successful. You can now log in.")

# Authenticate a user
def authenticate_user(username, password):
    users = load_user_data()
    if username in users:
        stored_password = users[username]["password"]
        if pbkdf2_sha256.verify(password, stored_password):
            return True
    return False

# Streamlit UI
st.title("User Authentication App")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
login_section = st.empty()  # Create an empty section for login

if menu == "Register":
    st.header("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.text_input("User Type")

    if st.button("Register"):
        if username and password and user_type:
            register_user(username, password, user_type)

if menu == "Login":
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success(f"Welcome, {username}!")
            login_section.empty()  # Clear the login section
        else:
            st.error("Authentication failed. Please check your credentials.")


# Uncomment the following line to display user data for debugging purposes.
st.write(load_user_data())