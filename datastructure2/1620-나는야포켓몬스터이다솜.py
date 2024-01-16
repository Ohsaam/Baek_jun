import sys

input = sys.stdin.readline

a,b = map(int,input().split())
data = {}


for i in range(1,a+1):
    word = input().rstrip()
    data[i] = word
    data[word] = i


for i in range(b):
    quest = input().rstrip() 
    if quest.isdigit():
        print(data[int(quest)])
        
    else:
        print(data[quest])