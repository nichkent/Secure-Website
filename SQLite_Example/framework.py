"""
Lab 8 Login Application

This is the file holds all the functions that will be executed in order to run the front end.
Includes home page, login page, create user page, and all the redirects that can be access from these pages.
"""

# Imports
import csv
from flask import Flask, render_template, request, url_for, flash, redirect
from config import display
from password_rules import hash_pw
import sqlite3
from database import add_user

# Controls the logout process
logout = 0

# assign the app variable
app = Flask(__name__)
# Assigns the reference to config.py
app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page
        Renders homepage
    """
    return render_template('home.html',
                           title="Home Page",
                           heading="Home Page",
                           show=display)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Login the user.
        renders login page and performs login actions.
    """
    # Will only run if the page is in a mode to receive information
    print(request.method)
    if request.method == 'POST':
        global logout
        if logout < 2:
            # Grabs user input
            username_user_input = request.form.get('username')
            password_user_input = request.form.get('password')

            # Hashes passwords and prepares them for comparisons
            password_hash_user_input, salt_length = hash_pw(password_user_input)
            password_hash_unsalted = password_hash_user_input[salt_length:]

            # Call to database
            conn = sqlite3.connect('member.db')
            c = conn.cursor()
            try:
                # Select query to search database to find something that matches the user's input
                result_username = c.execute("SELECT "
                                            "name FROM users WHERE users.name = "
                                            "'{username_string}';".format(username_string=username_user_input))
                # Assign the tuple to data_username
                database_username = result_username.fetchone()[0]

                # Grabs database username and compare it, if it passes goes to if block. If it fails the comparison it
                # Raises an error and reloads the page
                if database_username == username_user_input:
                    # Select statement that compares the user-input password that has now been hashed. Uses the LIKE
                    # Operator because the database password is salted. Searches for the user-input password string anywhere
                    # In the database.
                    result_password = c.execute("SELECT "
                                                "password FROM users WHERE users.password LIKE '%{passwrd_string}%';".format(passwrd_string=password_hash_unsalted))  # I don't think I can shorten these lines without breaking the code, sorry!
                    # Assigns database password tuple to database_password
                    database_password = result_password.fetchone()[0]

                    # Un-hashing database password
                    unhashed_database_password = database_password[salt_length:]

                    # Grabs database's password and compares to unsalted hash of password that the user entered,
                    # if it passes it goes to the next if block.
                    if unhashed_database_password == password_hash_unsalted:
                        # Select statement that finds the access level based on the username and password that have been
                        # compared to be true from the if statements above.
                        result_acc_level = c.execute("SELECT "
                                                     "access_level FROM users WHERE users.name = '{username}' "
                                                     "and users.password LIKE '%{passwrd_string}%';".format(username=username_user_input, passwrd_string=password_hash_unsalted))  # I don't think I can shorten these lines without breaking the code, sorry!
                        access_level_database = result_acc_level.fetchone()[0]

                        # Determines which of the four access levels the user has and redirects to the correct site
                        # Admin level
                        if access_level_database == 'AdminAccess':
                            return redirect(url_for('login_success_admin'))

                        # Engineering level
                        elif access_level_database == 'EngineeringAccess':
                            return redirect(url_for('login_success_engineering'))

                        # Accounting Access
                        elif access_level_database == 'AccountingAccess':
                            return redirect(url_for('login_success_accounting'))

                        # Basic access
                        elif access_level_database == 'BaseAccess':
                            return redirect(url_for('login_success_base'))

                # Execute sql commands
                conn.commit()
            except TypeError:
                logout += 1
                # Reloads the page if the user enters incorrect info
                return render_template('login.html')
        else:
            # If logout reaches 3, render logout.html
            return render_template('logout.html', title="Secure Logout", heading="Secure Logout")

    return render_template('login.html', title="Secure Login", heading="Secure Login")


@app.route("/login_success_admin", methods=['GET', ])
def login_success_admin():
    """ Login success Admin
        This is the redirection page if the users access level is Admin
    """
    return render_template('Admin_login.html',
                           title="Admin Home",
                           heading="Admin Home")


# Renders Engineering login screen from Engineering_login.html
@app.route("/login_success_engineering", methods=['GET', ])
def login_success_engineering():
    """ Login success engineering
        This is the redirection page if the users access level is Engineering
    """
    return render_template('Engineering_login.html',
                           title="Engineering Home",
                           heading="Engineering Home")


# Renders Accounting login screen from Accounting_login.html
@app.route("/login_success_accounting", methods=['GET', ])
def login_success_accounting():
    """ Login success Accounting
        This is the redirection page if the users access level is Accounting
    """
    return render_template('Accounting_login.html',
                           title="Accounting Home",
                           heading="Accounting Home")


# Renders Base user login screen from Base_login.html
@app.route("/login_success_base", methods=['GET', ])
def login_success_base():
    """ Login success Base
        This is the redirection page if the users access level is Base
    """
    return render_template('Base_login.html',
                           title="Base User Home",
                           heading="Base User Home")


# New User Creation method
@app.route("/create_new_user", methods=['GET', 'POST'])
def create_new_user():
    """ create_new_user
        This method query's the member database in order to add a new user. Takes a user-input to assign username and
        password, defines the access_level as BaseAccess (the lowest tier).
    """
    if request.method == 'POST':
        # Grabs user input
        username = request.form.get('username')
        password = request.form.get('password')

        add_user(username, password)
    return render_template('create_new_user.html',
                           title="Secure Login",
                           heading="Secure Login")
