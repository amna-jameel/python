# Q9. Student report card

# For each student, print the average (2 decimals) and Pass (60+) or Fail. At the end, print
# the topper.
# Expected: Ali 81.67 Pass · Sara 91.67 Pass · Ahmed 55.0 Fail · Topper: Sara

students = [
{"name": "Ali", "marks": [80, 75, 90]},
{"name": "Sara", "marks": [95, 88, 92]},
{"name": "Ahmed", "marks": [55, 62, 48]},
]
average=0
topper=""
highest_average=0
for std in students:
    name = std["name"]
    marks = std["marks"]
    average = sum(marks) /len(marks)
    if average>highest_average:
        highest_average=average
        topper=name
    if average>=60 :
        print(f"{name} {average} Pass! ")
    else :
         print(f"{name} {average} Fail! ")

    print(f"topper: {topper}")
   