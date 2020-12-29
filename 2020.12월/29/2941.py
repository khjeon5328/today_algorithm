import sys


sys.stdin = open('input.txt')

word = input()

# print(word)
cnt = len(word)

cro = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0
i = 0
while i < cnt:
    if i < cnt - 2:
        if word[i] + word[i+1] + word[i+2] == 'dz=':
            ans +=1
            i += 3
        elif word[i] + word[i+1] in cro:
            ans +=1
            i += 2
        else:
            if word[i].isalpha():
                ans += 1
            i += 1
    elif i < cnt - 1:
        if word[i] + word[i+1] in cro:
            ans +=1
            i += 2
        else:
            if word[i].isalpha():
                ans += 1
            i += 1
    else:
        if word[i].isalpha():
            ans += 1
        i += 1

print(ans)


