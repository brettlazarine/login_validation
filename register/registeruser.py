from database.db import (create_user, read_users, update_user, delete_user)
from emailvalidation.emailvalidation import email_is_valid
from passwordvalidation.passwordvalidation import password_is_valid

def register_user(email, password):
    if not email_is_valid(email):
        return "Email is not valid"
    pw_res = password_is_valid(password)
    if not pw_res[0]:
        return pw_res[1]
    
    user_emails = read_users("SELECT email FROM Users WHERE email = ?", email)
    if user_emails:
        return "Email already in use, please login or use a different email"
    
    query = "INSERT INTO Users (email, password) VALUES (?, ?)"
    params = (email, password)
    return create_user(query, params)