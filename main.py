import pyodbc
from config.config import load_config
from database.db import *

# ADMIN PRIVILEGES FOR SOME LOGINS THAT WOULD ALLOW ACCESS TO DATA ANALYTICS

def main():
    try:
        # READ USERS ***
        query = "SELECT * FROM Users"
        rows = read_users(query)
        if rows:
            for row in rows:
                print(row)
        else:
            print("No users found")
        
        # CREATE USER ***
        # query = "INSERT INTO Users (email, password) VALUES (?, ?);"
        # params = ('test2@test2.com', 'wxyz6789)')
        # res = create_user(query, params)
        # print(res)

        # UPDATE USER ***
        # query = "UPDATE Users SET email=? WHERE id=?;"
        # params = ('DeleteMe!', 3)
        # res = update_user(query, params)
        # print(res)

        # DELETE USER ***
        # query = "DELETE FROM Users WHERE id=?;"
        # params = (3)
        # res = delete_user(query, params)
        # print(res)

    except pyodbc.Error as e:
        print("Error: ", e)

        

if __name__ == "__main__":
    main()