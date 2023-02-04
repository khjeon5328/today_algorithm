import sys

sys.stdin = open('input.txt')
N = int(input())

x = y = 100
# print(x)
for _ in range(N):
    a, b = map(int, input().split())
    if a < b: x -= b
    elif a > b: y -= a
print(x)
print(y)
