#WAP to check whether the number entered by the user is even or odd.

Num = int(input("Enter a number: "))

if(Num % 2 == 0):
    print("The number entered is even.")
elif(Num % 2 != 0):
    print("The number entered is odd.")
else:
    print("The number entered is Invalid.")
    