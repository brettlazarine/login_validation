# ADMIN PRIVILEGES FOR SOME LOGINS THAT WOULD ALLOW ACCESS TO DATA ANALYTICS
from login.loginuser import login_user
from register.registeruser import register_user

def control_flow():
    print("Enter 1 to Login, 2 to Register, 3 to Exit")
    choice = input().strip()
    # USER EXITS
    if choice == "3":
        return (True, "Goodbye"), 3
    # USER REGISTERS
    elif choice == "2":
        print("Please enter your email")
        email = input().strip()
        print("""
Please enter a strong password:
    - Between 8 and 15 characters
    - At least one uppercase and one lowercase letter
    - At least one number and one special character
    - No spaces
              """)
        password = input()
        return register_user(email, password), 2
    # USER LOGS IN
    elif choice == "1":
        print("Please enter your email")
        email = input().strip()
        print("Please enter your password")
        password = input().strip()
        return login_user(email, password), 1
    else:
        return (True, "Invalid choice"), 3
    

def main():
    print("Welcome")
    while True:
        (success, res), exit_code = control_flow()
        print(res)

        if not success:
            continue

        if exit_code == 3:
            break
        if exit_code == 2:
            continue
        else:
            print("Press any key to continue")
            input()
            break
        

if __name__ == "__main__":
    main()