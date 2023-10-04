# while문으로 구현한 binary_search

def binary_search(arr, target, start, end):
  while start <= end: #while문의 종료는 start > end일 때 종료된다.
    mid = (start + end ) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] > target: # target이 왼쪽에 있을 경우
      end = mid -1
    else: # arr[mid] < target:
      start = mid + 1
  
  return None







n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = binary_search(arr,target, 0,n-1)

if result is None:
  print("값이 없음")
else:
  print(result + 1)


