# Create three variables: name, age, and city. Print them in a single sentence.
name = "Amna"
age = 20
city =  "Bahawalpur"
print("My name is" , name , ", age is" , age , "and city is " , city)

# Take your full name and print its length.
full_name = "Amna Jameel"
print("Length of the name is " , len(full_name))

# Reverse a string without using slicing.
reverse= " "
for name in full_name:
    reverse = name + reverse
    
print("With Loop :" ,reverse)
# with slicing 
print("Reverse of string :" , full_name[::-1])

# Count how many vowels are present in a string.
count = 0 
for name in full_name :
    if name.lower() in  "aeiou" :
        count = count+1

print(count)
 
    
# Take a sentence and count the number of words.
sen = "Salam ! I am Amna Jameel"
words = sen.split()
print(words)
print(len(words))
# Replace all spaces in a string with underscores.
sen = "Ben da iyyim.."
print(sen.replace(" " , "_"))

# Check whether a string is a palindrome.
string = "anna"
if string == string[::-1] :
    print("Palindrome")
else :
    print("Not a Palindrome")

# Extract the first, middle and last characters of a string.
name = "AMNAJ"
print("First character is " , name[0]) 
print("Last character is " , name[-1]) 
print("Middle character is " , name[len(name)//2]) 


