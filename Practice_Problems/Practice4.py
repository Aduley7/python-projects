Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))
Num4 = int(input("Enter the fourth number: "))

if(Num1 > Num2 and Num1 > Num3 and Num1 > Num4):
    print("The number 1 is the greatest")
elif(Num2 > Num1 and Num2 > Num3 and Num2 > Num4):
    print("The number 2 is the greatest")
elif(Num3 > Num1 and Num3 > Num2 and Num3 > Num4):
    print("The number 3 is the greatest")
else:
    print("The number 4 is the greatest")