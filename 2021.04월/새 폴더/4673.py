arr = [True] * 10001


def calc(n):
    hap = n
    while True:
        s, r = divmod(n, 10)
        hap += r
        n = s
        if not s:
            break
    return hap
# print(calc(9999))

i = 1
while i < 10001:
    selfNum = calc(i)
    if selfNum < 10001:
        arr[selfNum] = False
    i += 1
 

for i in range(1, 10001):
    if arr[i]:
        print(i)