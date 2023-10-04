T = int(input())
dp = []
for i in range(T):
    dp.append(list(map(int, input().split())))



for i  in range(1,T):
    for j in range(0,i+1):
        # 가장 왼쪽에 있는 경우
        if j == 0:
            dp[i][0] += dp[i-1][0] # 덧셈 전 부분  

        # 가장 오른쪽에 있을 경우
        elif i == j:
            dp[i][j] += dp[i-1][j-1]
        
        else: # 가운데 있을 경우[가지치기 경우의 수 고려 --> 가지치기 자체를 max로 선택]

            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[T-1]))


# 시간복잡도를 생각하자 -> O(n^2)