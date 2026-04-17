#Print Numbers from 1 to 100
# i = 1
# while i <=100:
#     print(i)
#     i += 1
    
#Print Numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
    
#Print the multiplication table of a number n
# n = int(input("Enter the number"))
# i = 1
# print("Table of 5 ")
# while i <= 10:
#     print(n*i) 
#     i += 1

#Print the elements of the following list using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# list = [1, 4, 9, 16, 25, 36, 64, 49, 81, 100]
# while i < len(list) :
#     print(list[i]) 
#     i += 1

#Search for a number x in this tuple using loop:
#tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 64
while i < len(tup):
    if(tup[i] == x):
        print("Found at index", i)
    i += 1