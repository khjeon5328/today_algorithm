import sys


sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    n, s = input().split()
    # print(n, s)
    p = ''
    for i in s:
        p += (i*int(n))
    print(p)