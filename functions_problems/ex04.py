# Exercise 4: Grade from marks Write grade(marks) that returns A (80+), B (70–79), C (60–69) or F (below 60). Test: grade(85) → A · grade(72) → B · grade(64) → C · grade(40) → F

def grade(marks):
    if marks>=80:
        return "A"
    elif marks>=70 and marks<=79:
        return "B"
    elif marks>=60 and marks<=69:
            return "C"
    elif marks<60:
            return f"{marks} F"
    else:
          return "Invalid input! please enter marks from 1-100"


print(grade(85))
print(grade(72))
print(grade(64))
print(grade(40))