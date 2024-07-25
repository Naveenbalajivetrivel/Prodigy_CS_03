import re

def is_password_strong(password):
    feedback = []

    # Check the length of the password
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    
    # Determine if the password is strong
    is_strong = len(feedback) == 0

    return is_strong, feedback

def main():
    password = input("Enter a password to assess its strength: ")
    is_strong, feedback = is_password_strong(password)

    if is_strong:
        print("Password is strong.")
    else:
        print("Password is not strong. Here are some suggestions to improve it:")
        for item in feedback:
            print(f" - {item}")

if __name__ == "__main__":
    main()
