import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

hap = int(input())

N =  int(input())

ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += a*b

if hap == ans:
    print('Yes')
else:
    print('No')