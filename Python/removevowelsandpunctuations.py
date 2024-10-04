x = input("Enter text")
for i in x:
    if i in "aeiou!@#$%^&*()":
        x = x.replace(i, "")
print(x)
