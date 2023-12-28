'''
2100017810 刘思瑞
'''
import math
while True:
    N = int(input())
    if N == 0:
        break
    summary = []
    for i in range(N):
        v,t = map(int,input().split())
        summary.append([t,t+(4.5/v)*3600,v])
    minn = 10**7
    for i in summary:
        if i[1]>0 and i[0]>=0:
            minn = min(minn,i[1])
    print(math.ceil(minn))
