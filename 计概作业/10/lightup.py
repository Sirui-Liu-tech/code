'''
刘思瑞 2100017810
'''
n,m = map(int,input().split())
li = [0]
li += list(map(int,input().split())) + [m]
atime,parttime,maxtime=0,0,0
for i in range(n//2+1):
    atime+=li[2*i+1] - li[2*i]
maxtime = atime
for i in range(n//2+1):
    parttime += li[2*i+1] - li[2*i]
    maxtime = max(max(m-li[2*i+1]-1-atime+parttime,atime-parttime)+parttime,maxtime)
print(maxtime)

