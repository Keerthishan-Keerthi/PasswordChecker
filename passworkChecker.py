import re

# Common weak passwords (can be extended from datasets like RockYou)
weak_passwords = {"password", "123456", "123456789", "qwerty", "abc123", "letmein"}

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (use at least 8 characters).")

    # Check for lowercase, uppercase, numbers, special characters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add digits.")
    
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Add special characters (@$!%*?&).")

    # Check against weak password list
    if password.lower() in weak_passwords:
        feedback.append("This password is too common! Choose something unique.")
        score = 0  # Force weak if it's in the list

    # Strength levels
    if score >= 6:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback


# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, suggestions = check_password_strength(pwd)
    print(f"Strength: {result}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")
