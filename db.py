import sqlite3
import bcrypt
import os

#use these to make sure we can access files in the local folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "users.db") 

def connect_db():
    return sqlite3.connect(DB_FILE)

def register_user(username, password, role="user"):
    conn = connect_db()
    cursor = conn.cursor()
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    try:
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", 
                       (username, password_hash, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT password_hash, role FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        hashPass = result[0]
        userRole = result[1] 
        
        if result and bcrypt.checkpw(password.encode(), hashPass.encode()):
            return True, userRole
        return False, None
    finally:
        conn.close()

def get_user_role(username):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT role FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        userRole = result[0] 
        return userRole if result else None
    finally:
        conn.close()
