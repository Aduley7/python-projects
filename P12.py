#WAP to find factorial of n.

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
cal_fact(7)

#WAP to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 94
    print(usd_val, "USD =", inr_val, "INR")
    
converter(50)

#H/W WAP to check if the number is ODD or EVEN

def odd_even(num):
    if(num%2==0):
        print(num, "is EVEN")
    else:
        print(num, "is ODD")
        
odd_even(76)