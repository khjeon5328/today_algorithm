import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

h, m = map(int, input().split())
t = int(input())

h2, m2 = divmod(t, 60)

h3 = h + h2 + (m+m2)//60
print(h3%24, (m+m2)%60)


