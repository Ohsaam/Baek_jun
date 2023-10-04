#입력 : 첫째 줄에 테스트 케이스의 개수 T + 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나
#출력 : 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력

n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i