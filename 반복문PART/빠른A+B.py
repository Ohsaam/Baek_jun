import sys

a = int(sys.stdin.readline())
sum = 0

for i in range(a):
    b, c = list(map(int, sys.stdin.readline().split()))
    sum = b+c
    print(sum)
    
