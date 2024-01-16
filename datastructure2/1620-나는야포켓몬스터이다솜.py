import sys

a,b = map(int,sys.stdin.readline().split())
print(a)
print(b)
data = []
for i in range(a):
    data.append(input())
    print(data[i])
