import streamlit as st
import pandas as pd
import os

# Define function to save user data to CSV file
def save_data(name, nickname, department, skill_interest, learning_power, email):
    user_data = {'Name': [name], 'Nickname': [nickname], 'Department': [department], 'Skill/Interest': [skill_interest], 'Learning Power': [learning_power], 'Email': [email]}
    df = pd.DataFrame(user_data)
    if not os.path.exists('users.csv'):
        df.to_csv('users.csv', index=False)
    else:
        df.to_csv('users.csv', mode='a', header=False, index=False)

# Define function to display registered users
def show_users():
    users_df = pd.read_csv('users.csv')
    users_df.drop(columns=['Name'], inplace=True)
    st.table(users_df)

# Set up Streamlit app
st.set_page_config(page_title="User Registration App", page_icon=":guardsman:", layout="wide")
st.title('User Registration App')
menu = ['Register', 'List Registered Users']
choice = st.sidebar.selectbox('Select an option:', menu)

if choice == 'Register':
    # Add input fields for user data
    name = st.text_input('Name')
    nickname = st.text_input('Nickname')
    department = st.selectbox('Department', ['Management', 'Engineering', 'Medical'])
    skill_interest = st.text_input('Skill/Interest')
    learning_power = st.selectbox('Learning Power', ['No', 'Weak', 'So-so', 'Strong'])
    email = st.text_input('Email')

    # Add submit button to save user data
    if st.button('Submit'):
        save_data(name, nickname, department, skill_interest, learning_power, email)
        st.success('Data saved successfully!')

elif choice == 'List Registered Users':
    # Add button to display registered users
    if st.button('View Registered Users'):
        show_users()
