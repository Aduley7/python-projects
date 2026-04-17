#WAP to find the greatest of three numbers entered by the user.

Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))

if(Num1 > Num2 and Num1 > Num3):
    print("The greatest number is", Num1)
    
elif(Num2 > Num1 and Num2 > Num3):
    print("The greatest number is", Num2)
    
else:
    print("The greatest number is", Num3)
        