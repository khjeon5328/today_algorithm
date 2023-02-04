import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
# print(lst)

permutation = []
idx = 0
for _ in range(N):
    cnt = 0
    while True:
        if lst[idx]:
            cnt += 1
            if cnt == K:
                break
        idx += 1
        idx %= N
    permutation.append(lst[idx])
    lst[idx] = 0
    # print(lst)
# print(permutation)

print('<', end="")
for i in range(N):
    if not i == N-1:
        print(permutation[i], end=", ")
    else:
        print(permutation[i], end="")
print('>')