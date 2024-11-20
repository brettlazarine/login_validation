from database.db import (create_user, read_users, update_user, delete_user)
from emailvalidation.emailvalidation import email_is_valid
from passwordvalidation.passwordvalidation import password_is_valid

def register_user(email, password):
    if not email_is_valid(email):
        return "Email is not valid"
    pw_is_valid, pw_message = password_is_valid(password)
    if not pw_is_valid:
        return pw_message
    
    user_emails = read_users("SELECT email FROM Users WHERE email = ?", email)
    if user_emails:
        return "Email already in use, please login or use a different email"
    
    query = "INSERT INTO Users (email, password) VALUES (?, ?)"
    params = (email, password)
    return create_user(query, params)