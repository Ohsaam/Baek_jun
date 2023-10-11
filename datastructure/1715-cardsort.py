import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
  a = int(input())
  heapq.heappush(card,a)

rs = 0

while len(card) > 1:
  n1 = heapq.heappop(card)
  n2 = heapq.heappop(card)
  rs += n1+n2
  heapq.heappush(card,n1+n2)
print(rs)

# 왜 rs가 아니라 n1+n2인가?
# 힙 자료구조의 조건은 항상 루트 노드가 
# 가장 작은 값을 가져야 한다
# rs를 추가하면 이 조건을 만족하지 않을 수 있으므로 오류가 발생할 수 있다.
# n1 + n2를 heapq.heappush(card, n1 + n2)로 추가하여 항상 가장 작은 두 묶음을 합치고, 이를 힙 자료구조로 유지하는 것이 올바른 접근이다.
# 최소힙에 대한 공부가 필요함  + 완전이진트리 