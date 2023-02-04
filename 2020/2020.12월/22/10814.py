import sys

sys.stdin = open('input.txt')

N = int(input())
age = [[] for _ in range(201)]
for _ in range(N):
    a, b = input().split()

    age[int(a)].append(b)
for i in range(1, 201):
    if age[i]:
        for j in age[i]:
            print(i, j)