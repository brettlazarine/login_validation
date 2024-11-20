from database.db import (read_users)

def login_user(email, password):
    query = "SELECT * FROM users WHERE email = ?"
    res = read_users(query, email)
    if not res:
        return False, "Email not found, please try again or register"
    pw = res[0][2]
    if password != pw:
        return False, "Incorrect password"
    return True, "Login successful"