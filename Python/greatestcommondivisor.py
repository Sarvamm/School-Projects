#greatest common divisor
import random
num1 = random.randint(0,50)
num2 = random.randint(50,100)
print(num1, num2)

for i in range(num1, 0, -1):
    if (num1%i == 0 and num2%i==0):
        c=i
        break
print("greatest common divisor is ",c)