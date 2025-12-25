import hashlib
import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak: No uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: No lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: No number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: No special character"
    return "Strong"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

print("=== Password Strength Analyzer ===")
password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
print("SHA-256 Hash:", hash_password(password))