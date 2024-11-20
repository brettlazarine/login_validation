from email_validator import validate_email, EmailNotValidError

def email_is_valid(email):
    try:
        valid = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False