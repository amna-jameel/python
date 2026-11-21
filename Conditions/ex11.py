# Exercise 11: University admission
# A student is eligible if (Matric 60% or above and Inter 50% or above), or Entry test 70 or
# above. Take all three and print Eligible or Not eligible.
matric = int(input("Enter your matric marks: "))
inter = int(input("Enter your inter marks: "))
Entry_test = int(input("Enter your entery test marks: "))
matric_per = (matric*60)/100
inter_per = (inter*50)/100
while matric<0 or matric>1100 or  inter<0 or inter>1100 or  Entry_test<0 or Entry_test>100:
     print("Invalid please enter marks matric and inter from 0-1100 and entry test from 0-100")
     matric = int(input("Enter your matric marks: "))
     inter = int(input("Enter your inter marks: "))
     Entry_test = int(input("Enter your entery test marks: "))  
if matric>=matric_per and inter>=inter_per and Entry_test>=70:
    print("Eligible")
else :
     print('Not Eligible')
     