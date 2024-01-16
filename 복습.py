import sys

n = int(input())
word = input()
n_list = [0] * n 
stack = []


for i in range(n):
  n_list[i] = int(input())
  
for i in word:
  if 'A' <= i <= 'Z':
    stack.append(n_list[ord(i)-ord('A')])
    
  else:
    str2 = stack.pop()
    str1 = stack.pop()
    
    if i == "+":
      stack.append(str1+str2)
      
    elif i == "-":
      stack.append(str1-str2)
      
    elif i == "*":
      stack.append(str1*str2)
      
    elif i == "/":
      stack.append(str1/str2)
      
print('%.2f' %stack[0])  
    