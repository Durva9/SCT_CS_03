import re
import string


def assess_password_strength(password):
    """
    Assess the strength of a password based on multiple criteria
    Returns: strength score, strength level, and detailed feedback
    """
    score = 0
    feedback = []
    
    # Criteria 1: Length
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append("✓ Excellent length (12+ characters)")
    elif length >= 8:
        score += 2
        feedback.append("✓ Good length (8-11 characters)")
    elif length >= 6:
        score += 1
        feedback.append("⚠ Weak length (6-7 characters)")
    else:
        feedback.append("✗ Too short (less than 6 characters)")
    
    # Criteria 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        uppercase_count = len(re.findall(r'[A-Z]', password))
        feedback.append(f"✓ Contains uppercase letters ({uppercase_count})")
    else:
        feedback.append("✗ No uppercase letters")
    
    # Criteria 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        lowercase_count = len(re.findall(r'[a-z]', password))
        feedback.append(f"✓ Contains lowercase letters ({lowercase_count})")
    else:
        feedback.append("✗ No lowercase letters")
    
    # Criteria 4: Numbers
    if re.search(r'\d', password):
        score += 1
        number_count = len(re.findall(r'\d', password))
        feedback.append(f"✓ Contains numbers ({number_count})")
    else:
        feedback.append("✗ No numbers")
    
    # Criteria 5: Special characters
    special_chars = string.punctuation
    if re.search(f'[{re.escape(special_chars)}]', password):
        score += 2
        special_count = len([c for c in password if c in special_chars])
        feedback.append(f"✓ Contains special characters ({special_count})")
    else:
        feedback.append("✗ No special characters")
    
    # Bonus: Check for variety (mixed character types)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(f'[{re.escape(special_chars)}]', password))
    
    variety_count = sum([has_upper, has_lower, has_digit, has_special])
    if variety_count == 4:
        score += 2
        feedback.append("✓ Excellent variety (all character types)")
    elif variety_count == 3:
        score += 1
        feedback.append("✓ Good variety (3 character types)")
    
    # Determine strength level
    if score >= 10:
        strength = "VERY STRONG"
        color = "🟢"
    elif score >= 7:
        strength = "STRONG"
        color = "🔵"
    elif score >= 5:
        strength = "MODERATE"
        color = "🟡"
    elif score >= 3:
        strength = "WEAK"
        color = "🟠"
    else:
        strength = "VERY WEAK"
        color = "🔴"
    
    return score, strength, color, feedback


def get_password_suggestions():
    """Provide suggestions for creating strong passwords"""
    suggestions = [
        "1. Use at least 12 characters (longer is better)",
        "2. Mix uppercase and lowercase letters",
        "3. Include numbers (0-9)",
        "4. Add special characters (!@#$%^&*)",
        "5. Avoid common words or personal information",
        "6. Don't use sequential patterns (123, abc)",
        "7. Consider using a passphrase (e.g., 'Coffee@Morning#2024!')"
    ]
    return suggestions


def display_strength_meter(score, max_score=12):
    """Display a visual strength meter"""
    filled = int((score / max_score) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    return f"[{bar}] {score}/{max_score}"


def main():
    print("=" * 70)
    print("PASSWORD STRENGTH ASSESSMENT TOOL")
    print("=" * 70)
    
    while True:
        print("\n" + "=" * 70)
        print("MENU")
        print("=" * 70)
        print("1. Check password strength")
        print("2. View password strength tips")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            print("\n" + "-" * 70)
            password = input("Enter a password to assess: ").strip()
            
            if not password:
                print("⚠ Password cannot be empty!")
                continue
            
            # Assess the password
            score, strength, color, feedback = assess_password_strength(password)
            
            # Display results
            print("\n" + "=" * 70)
            print("PASSWORD STRENGTH ASSESSMENT RESULTS")
            print("=" * 70)
            
            print(f"\nPassword: {'*' * len(password)} (hidden for security)")
            print(f"Length: {len(password)} characters")
            
            print(f"\nStrength Level: {color} {strength}")
            print(f"Strength Score: {display_strength_meter(score)}")
            
            print("\nDetailed Analysis:")
            print("-" * 70)
            for item in feedback:
                print(f"  {item}")
            
            # Recommendations
            print("\n" + "-" * 70)
            if score < 7:
                print("RECOMMENDATIONS:")
                if len(password) < 12:
                    print("  • Increase password length to at least 12 characters")
                if not re.search(r'[A-Z]', password):
                    print("  • Add uppercase letters (A-Z)")
                if not re.search(r'[a-z]', password):
                    print("  • Add lowercase letters (a-z)")
                if not re.search(r'\d', password):
                    print("  • Add numbers (0-9)")
                if not re.search(f'[{re.escape(string.punctuation)}]', password):
                    print("  • Add special characters (!@#$%^&*)")
            else:
                print("✓ Great password! Your password meets security standards.")
            
            print("=" * 70)
        
        elif choice == '2':
            print("\n" + "=" * 70)
            print("PASSWORD STRENGTH TIPS")
            print("=" * 70)
            suggestions = get_password_suggestions()
            for suggestion in suggestions:
                print(f"\n{suggestion}")
            
            print("\n" + "-" * 70)
            print("EXAMPLES OF STRONG PASSWORDS:")
            print("-" * 70)
            examples = [
                "MyDog@2024Runs!Fast",
                "Coffee#Morning$2024",
                "Tr@vel&Learn*2024!",
                "B!cycle#Ride$Sun123"
            ]
            for i, example in enumerate(examples, 1):
                print(f"{i}. {example}")
            
            print("\n" + "-" * 70)
            print("WHAT TO AVOID:")
            print("-" * 70)
            avoid = [
                "✗ Password123",
                "✗ qwerty",
                "✗ 123456",
                "✗ YourName123",
                "✗ birthday dates"
            ]
            for item in avoid:
                print(f"  {item}")
            print("=" * 70)
        
        elif choice == '3':
            print("\n" + "=" * 70)
            print("Thank you for using Password Strength Assessment Tool!")
            print("Stay secure! 🔒")
            print("=" * 70)
            break
        
        else:
            print("\n⚠ Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()