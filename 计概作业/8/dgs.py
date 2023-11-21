'''
刘思瑞 2100017810
'''
testnum = int(input())
for i in range(testnum):
    n ,m ,b = map(int,input().split())
    release = []
    time = []
    flag = 1
    for j in range(n):
        t , hurt = map(int,input().split())
        if t in time:
            release[time.index(t)].append(hurt)
        else:
            time.append(t)
            release.append([hurt])
    l = len(time)
    for j in range(l-1):
        for k in range(l-2-j):
            if time[k] > time[k+1]:
                time[k] , time[k+1] , release[k] , release[k+1] = time[k+1] , time[k] , release[k+1] , release[k]
    for j in range(l):
        release[j].sort(reverse = True)
        hurting = sum(release[j][:m])
        if hurting >= b:
            print(time[j])
            flag = 0
            break
        else:
            b -= hurting
    if flag:
        print('alive')

