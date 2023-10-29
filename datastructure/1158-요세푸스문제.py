import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())
que = deque()
rs = []
for i in range(1,n+1):
  que.append(i)

while que: # 사람이 존재 할 동안 
  for _ in range(k-1):
    que.append(que.popleft()) # 사람을 뒤에 보내는 코드
  rs.append(que.popleft())# 해당 부분이 k번째 사람을 제거하고 배열 rs에 추가한다.

print(str(rs).replace('[','<').replace(']','>'))

