a = input("Enter a string:")
b = len(a)
c = []
for i in range(0, b):
    for j in range(i+1, b):
        if a[i] == a[j]:
            c.append(j)
d = min(c)
print(a[d])




