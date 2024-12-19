import hashlib

import GUI
import sqlite3
import os


def create_user_account(entries):
    username = entries["Username"]

    con = sqlite3.connect("userdata.db")

    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS userdata(First_Name, Last_Name, Age, Email, Username, Password, Salt)''')

    cur.execute("SELECT 1 FROM userdata WHERE lower(Username) = lower(?)", (username,))
    if cur.fetchone():
        con.close()
        return False

    hashed_pw, salt = hashing_function(entries["Password"])
    entries["Password"] = hashed_pw
    entries["Salt"] = salt

    query = '''INSERT INTO userdata (First_Name, Last_Name, Age, email, username, password, salt) VALUES (:First_Name, 
    :Last_Name, :Age, :Email, :Username, :Password, :Salt)'''

    cur.execute(query, entries)

    con.commit()
    con.close()
    return True


def hashing_function(password, salt=None):
    b_password = password.encode()  # Turns string into bytes

    if salt is None:
        salt = os.urandom(16)
    else:
        salt = bytes.fromhex(salt)

    hashed_pw = hashlib.scrypt(password=b_password, salt=salt, n=16384, r=8, p=3)
    hex_hashed_pw = hashed_pw.hex()
    hex_salt = salt.hex()

    return hex_hashed_pw, hex_salt


def login_verification(username, password):
    con = sqlite3.connect("userdata.db")

    cur = con.cursor()

    query = """SELECT password, salt FROM userdata WHERE username = ?"""

    cur.execute(query, (username,))

    db_password, db_salt = cur.fetchone()

    entry_password, stored_salt = hashing_function(password, db_salt)

    if entry_password == db_password:
        return True
    else:
        return False


def main():
    GUI.create_login_window()


if __name__ == '__main__':
    main()
