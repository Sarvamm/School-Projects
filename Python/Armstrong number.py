#Check whether armstrong number or not
import math
x  = int(input("Enter a random number"))
digits =  int(math.log10(x)) + 1
r, num = 0,x

while num/10 > 0:
    r = r + (num%10)**digits
    num = num//10
if r == x:
    print("Armstrong number")
else:
    print("Non-armstrong number")