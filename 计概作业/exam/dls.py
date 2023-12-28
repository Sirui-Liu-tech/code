n,m,L = map(int,input().split())
l = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
for i in l:
    i.sort()
start = int(input())
vis = set()

def dls(s,deep):
    global l,vis,n,m,L
    if deep > L:
        return
    vis.add(s)
    print(s,end=' ')
    for i in l[s]:
        if i not in vis:
            dls(i,deep+1)
    return

dls(start,0)