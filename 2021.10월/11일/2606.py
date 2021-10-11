import sys



sys.stdin = open('input.txt')


n = int(input())
s = int(input())

q = [[] for _ in range(n+1)]

for _ in range(s):
    a, b = map(int, input().split())
    q[a].append(b)
    q[b].append(a)

# print(q)

visited = [0] * (n+1)
visited[1] = 1
ans = 0
def dfs(n):
    global visited, ans

    for i in q[n]:
        if not visited[i]:
            # print(i)
            ans +=1
            visited[i] = 1
            dfs(i)

dfs(1)
# print(visited)
print(ans)