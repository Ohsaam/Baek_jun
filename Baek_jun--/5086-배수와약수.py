while (1):
    x,y = map(int,input().split())
    
    if x==0 and y==0: # 마지막 줄에는 0이 2개 주어진다.
        break 
        
    if x<y and y%x==0: #첫 번째 숫자가 두  번째 숫자의 약수이다.
        print("factor")
    elif x>y and x%y==0: # 첫 번째 숫자가 두 번째 숫자의 배수이다.
        print("multiple")
    else: # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 둘 다 아니다.
        print("neither")
        
