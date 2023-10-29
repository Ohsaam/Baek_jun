# 알고리즘 설계 
# 1. 우리는  [4, 3, 6, 8, 7, 5, 2, 1] 결과를 Stack이라는 자료구조를 통해 구현해야한다.
# - Stack.append(UserInput) ---> op.append('+')
# - Stack[-1](Top) == UserInput: ---> op.append('-') 

# 변수 
# Flag : boolean / stack = [] / op = [] , num(핵심 key --> 비교)


n = int(input())
stack = [] 
op = [] 
flag = 0 
cur = 1

for i in range(n):
  num = int(input()) # 사용자로부터 입력받음
  while cur <= num:
    stack.append(cur) # 1 2 3 4 5 6 7 8 9 
    op.append("+") # 성공적으로 append 됐기 때문에 '+' --> 이제 조건 분기를 통해서 나눈다.
    cur += 1

  if stack[-1] == num:
    stack.pop()
    op.append("-") # Stack의 최댓값일 때, pop하는 알고리즘 적용한다.
    
  else:
    print("NO")
    flag = 1
    break


if flag == 0:
  for i in op:
    print(i)