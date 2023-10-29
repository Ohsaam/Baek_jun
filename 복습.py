
# 1. 알고리즘 설계
import sys

input = sys.stdin.readline

cnt = 1
flag = 0 #  설정
stack = []
op = []

n = int(input())
for i in range(n):
  num = int(input()) # 사용자가 값을 입력 
  while cnt <= num:
    stack.append(cnt) # 스택을 넣었다가 뽑아늘어놓음으로써 -> hint
    op.append('+')
    cnt += 1 

  if stack[-1] == num:
    stack.pop()
    op.append('-')

  else:
    print("NO")
    flag = 1
    break

if flag == 0:
  for i in op:
    print(i)


