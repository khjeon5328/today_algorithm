import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
path = [[] for _ in range(N+1)]
for i in range(N):
    path[i+1].append(int(input()))
# print(path)

ans = [0] * (N+1)
def dfs(idx, comb):
    global ans
    if path[idx][0] == comb[0]:
        for i in comb:
            ans[i] = 1
        return
    if path[idx][0] not in comb:
        comb.append(path[idx][0])
        dfs(path[idx][0], comb)
    else:
        return

for i in range(1, N+1):
    dfs(i, [i])
print(sum(ans))
for i in range(1, N+1):
    if ans[i]:
        print(i)