from collections import defaultdict,Counter
cnt = defaultdict(int)
for k in range(4):
    s = input()
    for i in s:
        if i == ' ':
            continue
        cnt[i.upper()]+=1

m = max(cnt.values())
l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(m):
    for j in l:
        if cnt[j] >= m-i:
            print('*',end='')
        else:
            print(' ',end='')    
        print(' ',end='')
    print('')
for i in l:
    print(i,end=' ')
