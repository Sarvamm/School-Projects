x = input("Enter text")
for i in x:
    if i in "AEIOUaeiou!@#$%^&*()":
        x = x.replace(i, "")
print(x)
