'''
2100017810 刘思瑞
'''
num = int(input())
m = list(map(int,input().split()))
count =   1  
dp = [0]*num
for i in range(num):
    temp = [1]
    for j in range(i):
        if m[i] <= m[j] :
            temp.append(dp[j]+1)
            if dp[j] + 1 >count:
                count = dp[j] + 1
    dp[i] = max(temp)

print(max(dp))