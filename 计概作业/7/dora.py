'''
刘思瑞 2100017810
'''
def find(n,l):
    maxx = n
    minn = 1
    r = 0 
    p = n-1
    while minn<maxx:
        if l[r] == minn:
            minn += 1
            r += 1
        if l[p] == minn:
            p-= 1
            minn += 1
        if l[r] == maxx:
            maxx -= 1
            r += 1
        if l[p] == maxx:
            p-= 1
            maxx -= 1
        if (l[p] not in (maxx,minn)) and (l[r] not in (maxx,minn)):
            return r+1,p+1
    return -1,None
testnum = int(input())
for i in range(testnum):
    n = int(input())
    li = list(map(int,input().split()))
    l = li[:]
    maxx,minx = find(n,l)
    if minx:
        print(maxx,minx)
    else:
        print(-1)

