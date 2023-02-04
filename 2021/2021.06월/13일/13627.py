import sys

sys.stdin = open('input.txt')

N, R = map(int, input().split())
returns = list(map(int, input().split()))

if N == R:
    print('*')
else:
    for i in range(1, N+1):
        if i not in returns:
            print(i, end=" ")
