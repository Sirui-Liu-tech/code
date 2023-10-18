'''
刘思瑞 2100017810
'''
columnn = []
def dp(i,key):
    global columnn
    if i == n - 1:
        return
    if key == 2:
        return
    if columnn[i+1] >= columnn[i]:
        dp(i+1,key)
        return
    else:
        for j in range(i+1,n):
            if columnn[j] >= columnn[i]:
                for k in range(i+1, j):
                    columnn[k] = columnn[i]
                dp(j,key)
                return 
        key += 1
        columnn = columnn[::-1]
        dp(0,key)
        return
                


n = int(input())
columnn = list(map(int,input().split()))
a = sum(columnn)
dp(0,0)
print(sum(columnn)-a)
