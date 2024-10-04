#Projject by Sarvamm
x = eval(input("enter a list with 3 numbers"))
if len(x) != 3:
    print("Error: List should contain exactly 3 numbers")
elif len(x) == 3:
    for i in x:
        if type(i) != int:
            print("Error: List should contain only integers")
            break
        
    c = x.pop(x.index(max(x)))
    a, b = x[0], x[-1]
    if c**2 == a**2 + b**2:
        print("The three numbers are a pythagorean triplet")
    else:
        print("The three numbers are not a pythagorean triplet")