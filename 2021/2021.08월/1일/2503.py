import sys
from itertools import permutations

sys.stdin = open('input.txt')

N = int(input())

per = list(permutations(range(1, 10), 3))
# print(per)


for _ in range(N):
    num, s, b = map(int, input().split())
    num = list(str(num))

    remove_cnt = 0

    for i in range(len(per)):
        i -= remove_cnt
        s_cnt = b_cnt = 0
        for j in range(3):
            num[j] = int(num[j])
            if num[j] in per[i]:
                if j == per[i].index(num[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != s or b_cnt != b:
            per.remove(per[i])
            remove_cnt += 1

print(len(per))

