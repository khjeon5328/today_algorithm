import sys


sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    n1, n2 = map(int, input().split())
    print(f'Case #{i+1}: {n1+n2}')