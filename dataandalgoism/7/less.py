'''
2100017810 刘思瑞
'''
n,k = map(int,input().split())
l = list(map(int,input().split()))
if k == 0:
    if 1 in l:
        print(-1)
    else:
        print(1)
elif k == n:
    print(max(l))
else:
    l.sort(reverse=-1)
    if l[n-k] != l[n-k-1]:
        print(l[n-k])
    else:
        print(-1)