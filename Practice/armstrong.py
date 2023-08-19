# Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
#
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

from math import pow

def is_armstrong(num):
    num = str(num)
    n = len(num)
    s = 0
    for i in num:
        s+=pow(int(i),n)

    if s == int(num):
        return True
    return False


resp = is_armstrong(10)

if resp:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")