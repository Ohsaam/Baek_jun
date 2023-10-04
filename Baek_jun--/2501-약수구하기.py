arr=[]
N, K = map(int, input().split())

for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)

if K > len(arr):
    print(0) #예외처리 
else:
    print(arr[K-1])