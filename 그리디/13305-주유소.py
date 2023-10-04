n = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))
minprice = price[0]
rs = 0

for i in range(n-1):
  if minprice > price[i]:
    minprice = price[i]
  rs += (minprice * city[i])
print(rs)