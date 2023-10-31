# 해당 문제를 풀 때 3가지를 고려해야된다. [스택 이용]

#  ')' -> '(' 일 경우  -> len(stack)
#  ')' -> ')' 일 경우  -> cnt+=1
word = input() # 문자열로 받는다. -> index -> for
stack = []
cnt = 0
# for문을 돌면서 -> 문자열 검사를 실시한다.

for i in range(len(word)): #word를 쪼개면서 진행한다.
  if word[i] == '(':
    stack.append(word[i]) # i는 안되는가?

  else: #이렇게 조건을 주는 것 자체가 ')'을 내포한다.
    if word[i-1] == '(':
      stack.pop(-1) # top을 pop한다.
      cnt += len(stack) 
    
    else: # word[i-1] == ')' 일  경우
      stack.pop(-1)
      cnt += 1

print(cnt)





