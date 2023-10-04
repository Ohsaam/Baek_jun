# 9×9 격자판에 쓰여진 81개의 자연수 
# 최댓값이 몇 행 몇 열에 위치한 수
table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = table[row][col]

print(max_num)
print(max_row, max_col)

