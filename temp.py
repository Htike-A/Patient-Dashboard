import sqlite3
import bcrypt
import os

# Ensure database is saved in the v1.1 directory
SCRIPT_DIR = r"C:\Users\conne\OneDrive - UWE Bristol\Uni\Year 2\AS\v1.1"
DB_FILE = os.path.join(SCRIPT_DIR, "users.db")  # Full path to database

def initialize_db():
    """Creates the database and users table if it does not exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database and users table created (if not already existing).")

def add_user(username, password, role="admin"):
    """Add a user with a hashed password and role."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Hash password before storing
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    try:
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", 
                       (username, password_hash, role))
        conn.commit()
        print(f"✅ User '{username}' added successfully with role '{role}'!")
    except sqlite3.IntegrityError:
        print("⚠️ Error: Username already exists.")

    conn.close()

# Step 1: Initialize the database
initialize_db()

# Step 2: Add an admin user
username = "admin"  # Change to the desired username
password = "password123"  # Change to a secure password

add_user(username, password, role="admin")
