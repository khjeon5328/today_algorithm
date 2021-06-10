import sys

sys.stdin = open('input.txt')

H, W, Y, X = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H+Y)]
# print(B)

A = [[0] * (W) for _ in range(H)]
for i in range(Y):
    for j in range(W):
        A[i][j] = B[i][j]

for i in range(H):
    for j in range(X):
        A[i][j] = B[i][j]
# print(A)

for i in range(Y, H):
    for j in range(X, W):
        A[i][j] = B[i][j] - A[i-Y][j-X]
# print(A)
for i in A:
    print(*i)
