import pyodbc
from config.config import load_config

def get_connection():
    config = load_config()
    conn_string = config["database"]["connectionString"]
    return pyodbc.connect(conn_string)

def create_user(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                conn.commit()
        return "User created successfully"
    except pyodbc.Error as e:
        return f"Error: {e}"

def read_users(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                rows = cursor.fetchall()
                return rows
    except pyodbc.Error as e:
        print(f"Error: {e}")
        return False

def update_user(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                conn.commit()
        return "User updated successfully"
    except pyodbc.Error as e:
        return f"Error: {e}"

def delete_user(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                conn.commit()
        return "User deleted successfully"
    except pyodbc.Error as e:
        return f"Error: {e}"