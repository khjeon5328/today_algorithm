import sys


sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    # print(a, b)
    n1 = min(a, b)
    n2 = max(a, b)

    for i in range(1, n2 + 1):
        if (i * n1) % n2 == 0:
            print(i*n1)
            break