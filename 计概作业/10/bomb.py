'''
刘思瑞 2100017810
'''

li , xli ,yli = [],[],[]
maxx = 0
times = 0
for i in range(1025):
    li.append([0]*1025)
d = int(input())
num = int(input())
for g in range(num):
    x,y,i = map(int,input().split())
    for j in range(max(0,y-d),min(1025,y+d+1)):
        for k in range(max(0,x-d),min(1025,x+d+1)):
            li[j][k] += i
for i in range(1025):
    for j in range(1025):
        if li[i][j] >maxx:
            maxx = li[i][j]
            times = 1
        elif li[i][j] == maxx:
            times+=1
print(times,maxx)
