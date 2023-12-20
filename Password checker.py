import re

def is_strong_password(password):
    # Minimum length of 8 characters
    if len(password) < 8:
        return False
    
    # Should contain at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Should contain at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Should contain at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Should contain at least one special character
    special_characters = "!@#$%^&*()-=_+[]{}|;:'\",.<>/?"
    if not any(char in special_characters for char in password):
        return False
    
    # Should not contain spaces
    if ' ' in password:
        return False
    
    # If all criteria are met, the password is considered strong
    return True

# Get password from the user
password = input("Enter your password: ")

# Check password strength
if is_strong_password(password):
    print("Password is strong!")
else:
    print("Password is weak. Please follow the password requirements.")
