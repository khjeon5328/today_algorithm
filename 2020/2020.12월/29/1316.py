import sys

sys.stdin = open('input.txt')

ans = 0
N = int(input())
for _ in range(N):
    ans += 1
    word = input()
    visited = [word[0]]
    n = len(word)
    for i in range(1, n):
        if visited[-1] == word[i]:
            continue
        else:
            if word[i] in visited:
                ans -= 1
                break
            else:
                visited.append(word[i])
print(ans)
        
        