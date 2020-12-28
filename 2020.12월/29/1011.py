import sys

sys.stdin = open('input.txt')
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    diff = y - x
    cnt = 0
    i = 1
    while diff > 0:
        diff -= i
        cnt += 1
        if not cnt % 2:
            i += 1
    print(cnt)