import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


a, b = map(int, input().split())
n1 = min(a, b)
n2 = max(a, b)
# print(n1, n2)

maxV = 1 
i = 1
while i <= n1:
    if (n1 % i == 0) and (n2 % i == 0):
        # print(i)
        maxV = i
    i += 1

print(maxV)

i = 1
minV = n1 * n2
while i <= n2:
    if (n1 * i) % n2 == 0:
        # print(i)
        minV = n1 * i
        break
    i += 1

print(minV)

