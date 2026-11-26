# Q12. Password checker (bonus)
# Keep asking for a password until it is strong:
# at least 8 characters
# at least one digit
# at least one capital letter
# Loop over the characters with .isdigit() and .isupper(), and use True/False flags.
# Expected: pakistan → weak · Pak2026 → weak (too short) · Pakistan2026 → Password
# accepted

while True:
    password = input("Enter your password: ")

    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True

        if char.isupper():
            has_upper = True

    if len(password) >= 8 and has_digit and has_upper:
        print("Password accepted!")
        break

    else:
        print("Weak password! Try again.")

        if len(password) < 8:
            print("- Password must be at least 8 characters.")

        if not has_digit:
            print("- Password must contain at least one digit.")

        if not has_upper:
            print("- Password must contain at least one capital letter.")
