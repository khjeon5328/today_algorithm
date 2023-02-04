import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
import copy

N = int(input())
hills = []
for _ in range(N):
    hills.append(int(input()))

hills.sort()
# print(hills)

minV = sys.maxsize
i = 0
while i <= hills[-1] - 17:
    costs = []
    for h in hills:
        if h < i:
            costs.append(i - h)
        elif h > i + 17:
            costs.append(h - (i +17))
    
    cost = 0
    for c in costs:
        cost += c ** 2

    minV = min(cost, minV)
    i += 1

print(minV)
    


