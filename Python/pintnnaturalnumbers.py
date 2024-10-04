##Project by Sarvamm
#Print n natural numbers

#Using for loop
x = int(input("Enter a number"))
# for i in range(1,x+1):
#     print(i)

#Using Recursion
def pnn(x):
    if x == 0:
        return
    print(x, end=" ")
    x -= 1
    pnn(x)
pnn(x)