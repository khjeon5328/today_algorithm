import sys
from math import gcd

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
trees = []
for _ in range(N):
    tmp = int(input())
    trees.append(tmp)

trees.sort()
dist = []
for i in range(len(trees)-1):
    dist.append(trees[i+1] - trees[i])
# print(dist)
minV = dist[0]
for i in dist[1:]:
    minV = gcd(minV, i)

tree = trees[-1] - trees[0]
s = tree // minV
print(s+1 -len(trees))