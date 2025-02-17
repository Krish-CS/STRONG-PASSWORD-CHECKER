import re

def check_password_strength(password):
    """Checks password complexity and provides feedback."""
    
    # Define password strength criteria
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # If all conditions met, password is strong
    if all([length_ok, has_upper, has_lower, has_digit, has_special]):
        return "✅ Strong password! Well done. 🔒"
    
    # If not, provide improvement suggestions
    suggestions = []
    
    if not length_ok:
        suggestions.append("🔹 Make the password at least 8 characters long.")
    if not has_upper:
        suggestions.append("🔹 Add at least one uppercase letter (A-Z).")
    if not has_lower:
        suggestions.append("🔹 Add at least one lowercase letter (a-z).")
    if not has_digit:
        suggestions.append("🔹 Include at least one number (0-9).")
    if not has_special:
        suggestions.append("🔹 Use at least one special character (!@#$%^&* etc.).")
    
    return "⚠️ Weak password. Consider the following improvements:\n" + "\n".join(suggestions)

def main():
    print("🔑 Password Strength Checker 🔑\n")
    
    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ").strip()
        
        if password.lower() == 'exit':
            print("Goodbye! Stay secure. 🔐")
            break
        
        feedback = check_password_strength(password)
        print("\n" + feedback + "\n" + "-"*50)

if __name__ == "__main__":
    main()
