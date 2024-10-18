#list generation
l=[]
for i in range(1,11):
    l.append(["Multiples of: " + str(i)])
    for j in range(1,26):
        if j % i == 0:
            l[i-1].append(j)
print(l)