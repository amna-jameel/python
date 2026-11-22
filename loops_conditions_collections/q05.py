# Q5. Grade report from a dictionary
# Loop through it with .items() and print each name with a grade: A (80+), B (70–79), C (60–
# 69), F (below 60). Then print the class average.
# Expected: Ali A, Sara A, Ahmed B, Hina F, Bilal C and Average: 75.0

students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}
total=0
for std,  key in students.items(): 
    if key>=80:
        grade="A"
    elif key>=70 and key<=79:
        grade="B"
    elif key>=60 and key<=69:
        grade="C"
    else:
        grade="F"

     
    total+=key 
    print(f"{std} {grade}")
    
    
average = total/len(students)
    
print(f"Average: {average}")
    