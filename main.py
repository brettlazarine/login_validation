import pyodbc
import json

def load_connection():
    with open("appsettings.json", "r") as file:
        return json.load(file)

def main():
    config = load_connection()
    conn_string = config["database"]["connectionString"]
    try:
        conn = pyodbc.connect(conn_string)
        print("Connection successful")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        cursor.close()
        conn.close()
    except pyodbc.Error as e:
        print("Error: ", e)

        

if __name__ == "__main__":
    main()