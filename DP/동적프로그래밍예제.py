T = int(input()) # 5
arr = []

for i in range(T):
    a = map(int, input().split())
    arr.append(a) # 값을 저장한다.


def solution(arr):
    for i in range(len(arr)): # 배열의 전체적인 depth 파악 
        for j in range(i+1):
            #가장 왼쪽에 있는 경우
            if j == 0:
                arr[i][j] += arr[i-1][j]
            #맨 오른쪽에 있는 경우
            elif i == j:
                arr[i][j] += arr[i-1][-1]

            # 중간에 있는 경우 
            else:
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])



print(max(arr[-1]))
# ...

