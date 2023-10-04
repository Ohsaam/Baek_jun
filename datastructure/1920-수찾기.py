N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
M = int(input())
M_list = [list(map(int,input().split())) for i in range(M)]

for i in M_list:
  for j in A:
    if i == j:
      print(1)
    else:
      print(0)