x = []
y = []
z = []
for i in range (0,10):
    x.append(int(input()))
    y.append(x[i]%42)
    if y[i] not in z:
        z.append(int(y[i]))
print(len(z))

