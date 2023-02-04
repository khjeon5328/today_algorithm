import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline
from collections import deque
def check(visited):
    if not visited.count(0):
        return True
    else:
        return False

while True:
    N = int(input())
    if not N:
        break

    maze = [list(input().split()) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    q = deque()
    q.append((0, 0, visited))
    isExit = 'No'
    while q:
        room, money, visited = q.popleft()
        # print(room, money, visited)
        if maze[room][0] == 'E':
            visited[room] = 1
            if check(visited):
                isExit = 'Yes'
                break
            for i in range(2, len(maze[room])-1):
                if not visited[int(maze[room][i])-1]:
                    q.append((int(maze[room][i])-1, money, visited))
        elif maze[room][0] == 'L':
            visited[room] = 1
            if check(visited):
                isExit = 'Yes'
                break
            for i in range(2, len(maze[room])-1):
                if not visited[int(maze[room][i])-1]:
                    if money >= int(maze[room][1]):
                        q.append((int(maze[room][i])-1, money, visited))
                    else:
                        q.append((int(maze[room][i])-1,int(maze[room][1]), visited))
        elif maze[room][0] == 'T':
            if int(maze[room][1]) <= money:
                visited[room] = 1
                if check(visited):
                    isExit = 'Yes'
                    break
                for i in range(2, len(maze[room])-1):
                    if not visited[int(maze[room][i])-1]:
                        q.append((int(maze[room][i])-1, money - int(maze[room][i]), visited))
    print(isExit)