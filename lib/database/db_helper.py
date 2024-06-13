

import sqlite3

DB_NAME = 'medical_management.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def execute_query(query, params=()):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")

def fetch(query, params=()):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return []
