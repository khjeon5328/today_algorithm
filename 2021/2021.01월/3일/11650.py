import sys


sys.stdin = open('input.txt')

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x : x[1])
arr.sort(key = lambda x : x[0])
for i in arr:
    print(*i)