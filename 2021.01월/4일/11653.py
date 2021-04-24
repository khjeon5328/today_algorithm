import sys


sys.stdin = open('input.txt')

N = int(input())
while N != 1:
    for i in range(2, N+1):
        if not N % i:
            print(i)
            N //= i
            break
