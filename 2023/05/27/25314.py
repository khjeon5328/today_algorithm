import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


N = int(input())


n = N //4

for _ in range(n):
    print('long', end = ' ')
print('int')