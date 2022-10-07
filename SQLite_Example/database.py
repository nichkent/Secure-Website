"""
Example SQLite Python Database
==============================

Database for the website that holds all user's info including usernames, passwords, and access_levels
Methods:
    create_db()
    add_user(username, password)
    remove_table()
    query_db()

"""
# Import
import sqlite3
from password_rules import hash_pw


def create_db():
    """ Create table 'users' in 'member' database
        return: users
    """
    try:
        conn = sqlite3.connect('member.db')
        c = conn.cursor()
        # Drops table if it already exists
        c.execute("DROP TABLE IF EXISTS users")

        # Creates table
        users = """CREATE TABLE users(
                    name text,
                    password text,
                    access_level text
                    ); """
        conn.execute(users)

        # Returns the newly created table
        return users
    except BaseException:
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def add_user(username, password):
    """ Data insert into users table
        param: username : str, password : str
    """
    # Grab user inputs
    new_user = username
    new_pass = password
    access_level = 'BaseAccess'  # Assign the base access level

    # Hash and salt password
    new_hash_pass, salt_length = hash_pw(new_pass)
    new_str_hash_pass = str(new_hash_pass)

    # Inserts the information into a variable for easy passage of information
    data_to_insert = [(new_user, new_str_hash_pass, access_level)]

    try:
        print(data_to_insert)
        # SQL statements to execute as a query
        conn = sqlite3.connect('member.db')
        c = conn.cursor()
        # Adds information from data_to_insert into the table
        c.executemany("INSERT INTO users VALUES (?, ?, ?)", data_to_insert)
        conn.commit()

    except sqlite3.IntegrityError:
        print("Error. Tried to add duplicate record!")
    else:
        print("Success")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def remove_table():
    """ Data delete users table
    """
    try:
        # SQL query to delete the information in the users table
        conn = sqlite3.connect('member.db')
        c = conn.cursor()
        c.execute('DELETE FROM users')
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error. Tried to delete non-existent record")
    else:
        print("Success")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def query_db():
    """ Display all records in the users table
    """
    try:
        # SQL query to display the users table in the member database
        conn = sqlite3.connect('member.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM users"):
            print(row)
    except sqlite3.DatabaseError:
        print("Error. Could not retrieve data.")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
