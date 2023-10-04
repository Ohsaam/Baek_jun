import sys; readline = sys.stdin.readline

lines = list(map(int, readline().split()))
lines.sort()
cond = lines[0] + lines[1]
if cond <= lines[2]:
    print(lines[0] + lines[1] + cond - 1)
else:
    print(sum(lines))