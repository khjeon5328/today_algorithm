import sys


sys.stdin = open('input.txt')




from itertools import combinations

while True:
    tmp = list(map(int, input().split()))
    if not tmp[0]:
        break
    K = tmp[0]
    S = tmp[1:]
    comb = list(combinations(S, 6))
    for i in comb:
        print(*i)
    print()

    
