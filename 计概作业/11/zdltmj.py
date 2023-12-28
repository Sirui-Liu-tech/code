'''
刘思瑞 2100017810
'''
m,flag,N,M,summ = [],[],0,0,0
def search(i,j):
    global m,flag,N,M,summ
    if i != 0:
        if ((flag[i-1][j] == True) and (m[i-1][j] == 'W')):
            summ += 1
            flag[i-1][j] = False
            search(i-1,j)
        if ((flag[i-1][j+1] == True) and (m[i-1][j+1] == 'W')):
            summ += 1
            flag[i-1][j+1] = False
            search(i-1,j+1)
        if j != 0:
            if ((flag[i-1][j-1] == True) and (m[i-1][j-1] == 'W')):
                summ += 1
                flag[i-1][j-1] = False
                search(i-1,j-1)
    if ((flag[i][j+1] == True) and (m[i][j+1] == 'W')):
        summ += 1
        flag[i][j+1] = False
        search(i,j+1)
    if ((flag[i+1][j+1] == True) and (m[i+1][j+1] == 'W')):
        summ += 1
        flag[i+1][j+1] = False
        search(i+1,j+1)
    if ((flag[i+1][j] == True) and (m[i+1][j] == 'W')):
        summ += 1
        flag[i+1][j] = False
        search(i+1,j)
    if j != 0:
        if ((flag[i][j-1] == True) and (m[i][j-1] == 'W')):
            summ += 1
            flag[i][j-1] = False
            search(i,j-1)
        if ((flag[i+1][j-1] == True) and (m[i+1][j-1] == 'W')):
            summ += 1
            flag[i+1][j-1] = False
            search(i+1,j-1)
    return
    

num = int(input())
for k in range(num):
    m = []
    flag = []
    sum = 0
    N,M = map(int,input().split())
    for i in range(N):
        flag.append([True]*(M)+[False])
        s = input()
        temp = []
        for j in range(M):
            temp.append(s[j])
        temp.append('.')
        m.append(temp)
    m.append(['.']*(M+1))
    flag.append([False]*(M+1))
    for i in range(N):
        for j in range(M):
            if m[i][j] =='W' and flag[i][j] == True:
                summ = 1
                flag[i][j] = False
                search(i,j)
                sum = max(sum,summ)
    print(sum)
