'''
刘思瑞 2100017810
'''
def delete(n,m):
    flag = [True]*n
    j = 0
    times = 0
    sum = 0
    while True:
        if flag[j] == True:
            sum +=1
            if sum == m:
                flag[j] = False
                times += 1
                sum = 0
        if times == n-1:
            break
        if j == n-1:
            j = 0
        else:
            j+=1
    return flag.index(True) + 1


while True:
    n,m = map(int,input().split())
    if [n,m] == [0,0]:
        break
    print(delete(n,m))

