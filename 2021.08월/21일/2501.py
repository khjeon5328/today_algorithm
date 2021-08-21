import sys



sys.stdin = open('input.txt')

N, K = map(int, input().split())
# print(N, K)
cnt = 0
for i in range(1, N+1):
    if not N % i:
        cnt += 1
        if cnt == K:
            print(i)
            break

if cnt < K:
    print(0)