import sys


sys.stdin = open('input.txt')

word1 = input()
word2 = input()
N1 = len(word1)
N2 = len(word2)

arr = [[0]*(N2+1) for _ in range(N1+1)]
for i in range(1, N1 + 1):
    for j in range(1, N2 + 1):
        if word1[i-1] == word2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
# from pprint import pprint
# pprint(arr)
print(arr[-1][-1])