# 8 - 15 characters
# at least one uppercase letter
# at least one lowercase letter
# at least one digit
# at least one special character
# no whitespace

def password_is_valid(password):
    if len(password) < 8 or len(password) > 15:
        return (False, "Password must be between 8 and 15 characters")
    if not any(char.isupper() for char in password):
        return (False, "Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        return (False, "Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        return (False, "Password must contain at least one digit")
    if not any(not char.isalnum() for char in password):
        return (False, "Password must contain at least one special character")
    if any(char.isspace() for char in password):
        return (False, "Password must not contain any spaces")
    return (True, "Password is valid")