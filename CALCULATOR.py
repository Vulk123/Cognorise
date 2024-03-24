num1=float(input("Enter 1st number"))
num2=float(input("Enter 2nd number"))
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for exponential")
e=int(input(" "))
if(e==1):
     print(num1+num2)
elif(e==2):
     print(num1-num2)
elif(e==3):
     print(num1*num2)
elif(e==4):
     print(num1/num2)
elif(e==5):
     print(num1**num2)
else:
     print("INVALID")


