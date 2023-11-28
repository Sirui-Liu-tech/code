'''
刘思瑞 2100017810
'''
T,M = map(int,input().split())
li = []
value = 0
for i in range(M):
    t,m = map(int,input().split())
    li.append([t,m])
value = [[0]*(li[0][0]) + [li[0][1]]*(T+1-li[0][0])]
for i in range(len(li)-1):
    value.append([0]*(T+1))
for i in range(1,len(li)):
    for j in range(1,T+1):
        if j >= li[i][0]:
            value[i][j] = max(value[i-1][j],value[i-1][j-li[i][0]]+li[i][1])
        else:
            value[i][j] = value[i-1][j]
print(value[-1][-1])