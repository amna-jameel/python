# Exercise 8: Student profile (**kwargs)
# Write make_profile(**info) that prints every detail as key: value and returns how many
# details were given.
# Test: make_profile(name="Sara", city="Multan", course="Python") prints three lines
# (name: Sara, city: Multan, course: Python) and returns 3

def stud_profile(**profile):
    for key , value in profile.items():
        print(f"{key} : {value}")

    return len(profile)


total = stud_profile(name="Amna", Department="Computer science", Rollno=12, Specialization="all")
print(f"Total details given: {total}")