#1~n번까지의 번호가 매겨져 있다. 
#   1. 가장 처음 바구니에는 공이 들어있지 않으며,
#   2. 바구니에는 공을 1개만 넣을 수 있다. 
#   3. 


N,M = map(int,input().split())
basket = [i for i in range(N+1)]
tmp = 0


for i in range(M):
    i,j = map(int,input().split())
    tmp = basket[i-1]
    basket[i-1] =  basket[j-1]
    basket[j-1] = tmp
        

for i in range(N):
    print(basket[i], end = '')
    
    
    