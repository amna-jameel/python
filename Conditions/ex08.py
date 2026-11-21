# Exercise 8: Character type
# Take one character and print whether it is a Vowel, Consonant, Digit or Special character.
# Hint: .isdigit(), .isalpha(), and .lower() in "aeiou".
char = input("Enter a character: ")
if char.lower() in "aeiou" :
    print(f"{char} is a Vowel")
elif len(char)!=1 :
    print("Please enter only one character..")
elif char.isalpha():
    print(f"{char} is a Consonant")
elif char.isdigit():
    print(f"{char} is Digit")
else :
    print(f"{char} is a special character")