import sys


sys.stdin = open('input.txt')

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
# print(arr)
vowels = ['a', 'e', 'i', 'o', 'u']
def check(code):
    constant = vowel = 0
    for i in code:
        if i in vowels:
            vowel += 1
        else:
            constant += 1
        if vowel > 0 and constant > 1:
            return True
    return False



def dfs(n, idx, code):
    if n == L:
        if check(code):
            print(code)
        return
    for i in range(idx, C):
        dfs(n+1, i+1, code + arr[i])

dfs(0, 0, '')