import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    cnt = 0
    a, b = divmod(i, 10)
    while a:
        if b == 3 or b == 6 or b == 9:
            cnt += 1
        a, b = divmod(a, 10)
    if b == 3 or b == 6 or b == 9:
        cnt += 1
    if cnt:
        print('-'*cnt, end=" ")
    else:
        print(i, end=" ")