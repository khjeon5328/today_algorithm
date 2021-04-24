import sys

sys.stdin = open('input.txt')

T = int(input())

t = [(i*(i+1)//2) for i in range(1, 45)]
u = [0] * 1001
# print(len(u))
# print(t)
for i in t:
    for j in t:
        for k in t:
            hap = i + j + k
            if hap < 1001:
                u[hap] = 1
for _ in range(T):
    n = int(input())
    print(u[n])
    