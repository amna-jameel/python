
# Take two numbers and perform all arithmetic operations.
num1 = 20
num2 = 12
print("Addition: " , num1 + num2)
print("Subtraction: " , num1 - num2)
print("division(float): " , num1 / num2)
print("Division(decimal): " , num1 // num2)
print("Multiplication: " , num1 * num2)
print("Modulus: " , num1 % num2)

# Take a number and calculate its square and cube.
import math
num=4
squareroot=math.sqrt(num)
cube=math.cbrt(num)
print("square root:" , (squareroot))
print("cube root " , (cube))


# Convert a float number into an integer and print both values.
float_num = 12.09
integar = int(float_num)
print("Float number:" , float_num)
print("integar: " , integar)

# Find the remainder and quotient when 45 is divided by 6.
num1 = 45
num2 = 6
print("Remainder :" , num1% num2)
print("Quotient :" , num1 // num2)

# Use the math module to calculate the square root, factorial and power of a number.
import math
num = 4
squareroot = math.sqrt(num)
factorial = math.factorial(num )
power = math.pow(num ,2)
print("Square root " , squareroot)
print("Factorial " , factorial)
print("Power " , power)


# ceil , floor , trunc 
num= 3.4 
ceil = math.ceil(num)
floor =math.floor(num)
trunc=  math.trunc(num)
print("Ceil " , ceil)
print("floor " , floor)
print("trunc " , trunc)

# Random 
import random
randomnum = random.random()
randomint = random.randint(1,6)
teams = ["Amna" ,"Fiza" , "Ayesha"]
choice = random.choice(teams)
random.shuffle(teams)
print("Random" ,  randomnum)
print("Random int" ,  randomint)
print("Choice" ,  choice)
print("shuffle" ,  teams)
