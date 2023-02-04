import sys

sys.stdin = open('input.txt')

n, c = map(int, input().split())

numerator = 1
for i in range(c):
    numerator *= (n-i)
# print(numerator)
denominator = 1
for i in range(1, c+1):
    denominator *= i

print(numerator // denominator)