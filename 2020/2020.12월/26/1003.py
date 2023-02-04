import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        fibo = [[0, 0] for _ in range(n+1)]
        fibo[0] = [1, 0]
        fibo[1] = [0, 1]
        for i in range(2, n+1):
            fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
            fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]
        print(*fibo[n])