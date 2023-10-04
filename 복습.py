import sys
input = sys.stdin.readline
T = int(input())
dp = list(map(int,input().split()))

for i in range(1,T):
  dp[i] = max(dp[i],dp[i-1]+dp[i])
print(max(dp))