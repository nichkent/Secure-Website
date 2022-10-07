""""
password_rules.py holds hash_pw to manipulate passwords and return them for the login and create users functions
"""

# Import
import hashlib
import os
from base64 import b64encode


def hash_pw(plain_text) -> tuple[str, int]:
    """ hash_pw
        param: plain_text : str
        return: hashed_plain_text : str, salt_length : int
        hash_pw takes a plain_text password and hashes it, returning the newly salted password and salt_length
    """
    # Assigns the size in bytes for the urandom function
    size = 20
    salt_encoded = os.urandom(size)
    salt = b64encode(salt_encoded).decode('utf-8')
    salt_length = len(salt)  # Grab length of salt

    # Creating the hashable passwords
    plain_text = plain_text.encode('utf-8')
    hashed_plain_text = hashlib.sha1(plain_text).hexdigest()
    hash_pass = salt + hashed_plain_text  # concatenate salt and plain_text

    # Return vars
    return hash_pass, salt_length  # prepend hash and return

