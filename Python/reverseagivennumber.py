#Project by Sarvamm
#reverse a given number
import math
x = int(input("Enter a random number"))
# x = str(x)
# print(int(x[::-1]))
# r=""
# while x%10 > 0:
#     r = r + str(x%10)
#     x = x//10
# print(r)

#without using strings:
r, num  = 0 , x

k = int(math.log10(x))     # number of digits in the given number
while num/10 > 0: 
    r = r + (num%10)*(10**k)
    k -= 1
    num = num//10
print(r)