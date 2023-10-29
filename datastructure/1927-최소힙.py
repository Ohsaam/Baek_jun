import sys 
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  com = int(input())
  if com != 0:
    heapq.heappush(heap, com)
  
  else:
    try:
      print(heapq.heappop(heap))
    except:
      print(0)

