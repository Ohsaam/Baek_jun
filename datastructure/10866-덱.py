import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])

for i in range(n):
  com = input().split()
  if com[0] == "push_front":
    queue.appendleft(com[1])
  
  elif com[0] == "push_back":
    queue.append(com[1])
  
  elif com[0] == "pop_front":
    if len(queue) > 0:
      print(queue.popleft())
    else:
      print(-1)
    
  elif com[0] == "pop_back":
    if len(queue) > 0:
      print(queue.pop())
    else:
      print(-1)
  
  elif com[0] == "size":
    print(len(queue))
  
  elif com[0] == "empty":
    if len(queue) > 0:
      print(0)
    else:
      print(1)
  elif com[0] == "front":
    if len(queue) > 0:
      print(queue[0])
    else:
      print(-1)


  elif com[0] == "back":
    if len(queue) > 0:
      print(queue[-1])
    else:
      print(-1)



