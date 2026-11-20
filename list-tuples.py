# Exercise 1: City list 

cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"] 
print(cities)
print("first city: " ,  cities[0])
print("last city: " ,  cities[-1])
print("Middle three : " ,cities[1:4])
print("Reversed :" , cities[::-1])

# Exercise 2: Marks report 
marks = [78, 92, 65, 88, 54]  
total = 0
count = 0 
high = 0 
low = 0
for mark in marks:
    total = total + mark
    average = total/len(marks)
    if mark>high :
            high = mark 
    else :
         low = mark
    if mark>70 :
        count=count+1
   
print("Total :" , total)
print("Average :" , average)
print("Above 70 :" , count)
print("Highest :" , high)
print("Lowest :" , low)

# Exercise 3: Shopping list 
# Start with ["bread", "milk", "eggs"]. Then: 
# ● append "rice" 
# ● insert "sugar" at index 1 
# ● remove "milk" 
# ● pop() the last item and print what was popped 
# Expected: popped rice, final list ['bread', 'sugar', 'eggs']
shopping_list = ["bread", "milk", "eggs"]
print(shopping_list)
shopping_list.append("rice")
print(shopping_list)
shopping_list.insert(1, "sugar") 
print(shopping_list)
shopping_list.remove("milk")
print(shopping_list)
print(shopping_list , "popped item is : " , shopping_list.pop()) 

# Exercise 4: Remove duplicates 
nums = [3, 1, 3, 2, 1, 5] 
empty_list = []
for n in nums :
    if n not in empty_list:
        empty_list.append(n)
print(empty_list)


# Exercise 5: Even and odd (list comprehension)
even = [x for x in range (1,15) if  x%2==0 ]
print(even)
odd=[x for x in range (1,15) if  x%2!=0 ]
print(odd)


# Exercise 6: Rotate a list 
r = [1, 2, 3, 4, 5]
new = r[2:] + r[0:2] 
print(new)

# Exercise 7: Copy or not? 
a = [1, 2, 3]
b= a
c=a.copy()
a.append(4)
print(a)
print(b)
print(c)
# explain why b changed but c did not.
# b is the shallow copy of a , c is the deep copy thats it 

# Level 3: Tuples 
# Exercise 8: Student record 

student = ("BSIT-12", "Sara", 88) 
roll_no, name, marks = student
print(f"student name is {name} , roll_no is {roll_no} and marks are {marks}")
std_list = list(student)
std_list[2]=95
student = tuple(std_list)
roll_no, name, marks = student
print(student , type(student))
print(f"student name is {name} , roll_no is {roll_no} and marks are {marks}")


# Exercise 9: Vote counter 
votes = ("A", "B", "A", "C", "A", "B","A") 
count , count_B , count_C = 0 , 0 , 0
for n in votes :
    if "A" in n:
         count=count+1
    if "B" in n:
             count_B=count_B+1
    if "C" in n:
             index = votes.index(n)
             count_C=count_C+1
    
print("A=",count,"B=",count_B,"C=",count_C ,"first C at index" , index )


# Exercise 10: List of tuples 
students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)] 
topper = students[0]
# 1. Loop through the list and print each student as Ali scored 85. 
for std in students :
      print(f"{std[0]} scored {std[1]}")
# 2. Find the topper
     
      if std[1] > topper[1]:
        topper = std

print("Topper:", topper[0], topper[1])
# 3. Make a list of the names of students who passed (marks 70 or above). 
# Expected: topper Sara 92, passed ['Ali', 'Sara', 'Ahmed']


# Exercise 11: Second highest 
scores = [45, 82, 67, 91, 73] 
# Find the second highest score with a loop only. Don't use sort() or max(). 
# Expected: 82 
scores=list(scores)
high=[]
sec_high =[]
for mark in scores:
      if mark>high:
          high = high.append(mark)
    #   if  high > marj 
print(high)