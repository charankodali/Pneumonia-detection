import streamlit as st
import csv
import hashlib
import subprocess
import base64

original_title = '<b><center><p style="font-size: 60px; border-radius:50px 0px 50px 0px; color:black; background-color: #B5C0D0;">Pneumonia Detection</p></center></b>'
st.markdown(original_title, unsafe_allow_html=True)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:bgs/background.jfif;base64,%s");
        background-position: center;
        background-size: cover;
        }
        </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('bgs/background.jfif')

# CSS for styling the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#74EBD5, #ACB6E5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# CSV file path to store user information
csv_file_path = "user_database.csv"
main_script_path = "streamlit/Home.py"  # Path to the main script #changed path

# Check if 'user_database' is not already defined in session state
if 'user_database' not in st.session_state:
    # Initialize 'user_database' as an empty list
    st.session_state.user_database = []


def save_to_csv(username, hashed_password):
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])


def read_from_csv():
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        return {row[0]: row[1] for row in reader}


def hash_password(password):
    # Use a secure hash function like SHA-256
    return hashlib.sha256(password.encode()).hexdigest()


def launch_main_script():
    subprocess.run(["streamlit", "run", main_script_path])


def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if username and password and confirm_password:
            if password == confirm_password:
                if username not in st.session_state.user_database:
                    hashed_password = hash_password(password)
                    save_to_csv(username, hashed_password)
                    st.success("Account created successfully. Now you can log in.")
                else:
                    st.warning("Username already exists. Please choose a different username.")
            else:
                st.warning("Passwords do not match. Please enter matching passwords.")
        else:
            st.warning("Username, password, and confirm password are required for sign up.")    


def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        user_database = read_from_csv()
        if username in user_database:
            hashed_password = hash_password(password)
            if user_database[username] == hashed_password:
                st.success(f"Welcome, {username}!")

                # Launch the main script after successful login
                launch_main_script()
            else:
                st.error("Invalid password. Please try again.")
        else:
            st.error("Invalid username. Please try again.")


def main():
    st.title("Login and Signup App")

    # Create a sidebar for navigation
    menu = ["Sign Up","Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Display the selected page
    if choice == "Sign Up":
        signup()
    elif choice == "Login":
        login()  


if __name__ == "__main__":
    main()
