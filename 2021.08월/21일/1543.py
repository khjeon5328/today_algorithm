import sys



sys.stdin = open('input.txt')

words = input()
idx =  input()
# print(words, idx)

ans = 0
n = 0
while n <= len(words) - len(idx):
    if words[n:n+len(idx)] == idx:
        n += len(idx)
        ans += 1
    else:
        n += 1


print(ans)