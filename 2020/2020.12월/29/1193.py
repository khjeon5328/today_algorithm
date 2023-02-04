# import sys

# sys.stdin = open('input.txt')

N = int(input())
cnt = 0
hap = 0
while hap < N:
    cnt += 1
    hap = hap + cnt
    # print(hap, cnt)
# print(cnt)
diff = hap - N
if cnt % 2:
    print(f'{1+diff}/{cnt - diff}')
else:
    print(f'{cnt - diff}/{1+diff}')