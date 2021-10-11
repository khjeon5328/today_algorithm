import sys

sys.stdin = open('input.txt')

arr = list(input())
# print(arr)

def palindrom(lst):
    n = len(lst)//2
    for i in range(n):
        tmp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = tmp
    return lst
ans = [i for i in arr]
n = len(arr)
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            split1 = arr[:i+1]
            split2 = arr[j:k]
            split3 = arr[k:]
            tmp = palindrom(split1) + palindrom(split2) + palindrom(split3)
            # print(tmp)
            if tmp < ans:
                ans = tmp
    #         break
    #     break
    # break

print("".join(ans))