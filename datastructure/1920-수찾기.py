N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr=list(map(int,input().split()))
A.sort()

for num in arr:
  lt, rt = 0, N-1
  isExist = False

  while lt <= rt:
    mid = (lt + rt) // 2

    if A[mid] == num:
      isExist = True
      print(1)
      break
    elif A[mid] > num :
      rt = mid - 1
    else:
      lt = mid + 1
  if not isExist:
    print(0)