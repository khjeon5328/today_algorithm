import sys

sys.stdin = open('input.txt')

N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))
rank = []
for i in people:
    cnt = 1
    for j in people:
        if i != j:
            if i[0] < j[0]:
                if i[1] < j[1]:
                    cnt +=1
    rank.append(cnt)
print(*rank)