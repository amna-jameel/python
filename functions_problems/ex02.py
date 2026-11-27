# Exercise 2: Welcome message (default parameter) Write greet_student(name, course="Python") that returns a welcome message. If no course is given, use Python. Test: greet_student("Sara") → Welcome Sara to the Python class · greet_student("Ali", "Django") → Welcome Ali to the Django class

def greet_student(name , course="python"):
    print(f"Welcome {name} to the {course} class")

greet_student("Sara")
greet_student("ali", "Django")

