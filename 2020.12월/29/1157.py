import sys

sys.stdin = open('input.txt')

# import collections

# s = input().upper()
# ctn = collections.Counter(s)
# top = ctn.most_common(2)
# if top[0][1] == top[1][1]:
#     print('?')
# else:
#     print(top[0][0])

s = input().upper()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = []
maxV = 0
for k, v in d.items():
    if v > maxV:
        maxV = v
        ans = []
        ans.append(k)
    elif v == maxV:
        ans.append(k)
if len(ans) == 1:
    print(ans[0])
else:
    print('?')