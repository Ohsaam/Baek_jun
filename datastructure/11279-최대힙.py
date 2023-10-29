import sys
import heapq

input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
  num = int(input())

  if num != 0:
    heapq.heappush(queue, -num)

  else:
    try:
      print(-heapq.heappop(queue))
    except:
      print(0)