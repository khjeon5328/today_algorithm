import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

h, m, s = map(int, input().split(' '))
tt = int(input())
# print(h, m, s)
# print(tt)

q1, r1 = divmod(tt, 3600)
# print(q1, r1)
#q1은 시간
q2, r2 = divmod(r1, 60)
#q2는 분
#r2는 초
# print(q2, r2)

if r2 + s >= 60:
    s = r2 + s - 60
    q2 += 1
else:
    s += r2

if q2 + m >= 60:
    m = q2 + m - 60
    q1 += 1
else:
    m += q2

if q1 + h >= 24:
    h = q1 + h - 24
else:
    h += q1


print(h, m, s)
