def fibo(N):
  # case -1 : young_case = [1,0,1]
  # case -2 : il_case = [0,1,1]
  # 핵심 아이디어 : 각 case 별로 추가한다.
    # for문은 2 ~ N[사용자로부터 받음]까지 진행
  young_case = [1,0,1]
  il_case = [0,1,1]
  if N >= 3: # why 3보다 커야함? -> 피보나치 조건 check
    for i in range(2, N):
      young_case.append(young_case[i] + young_case[i-1])
      il_case.append(il_case[i] + il_case[i-1])
  
  print(f"{young_case[N]} {il_case[N]}")




T = int(input())

for _ in range(T):
  N = int(input())
  fibo(N)