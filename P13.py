#Recursion
 #recursive function
def show(n):
    if(n == 0): #Base case(as stopping condition is looping)
        return
    print(n)
    show(n-1)
    print("END")
    
# show(5)

 #Recurrance Relation(for factorial is n! = (n-1!) * n)
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n
# print(fact(2))


def calc_sum(num):
    if(num == 0):
        return 0
    return calc_sum(num-1) + num

# print(calc_sum(5))

#WA recursive function to print all elements in a list.
#Hint: use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits = ["Mango", "Litchi", "Apple", "Banana"]
print_list(fruits)