'''
刘思瑞 2100017810
'''
import sys
n,t = map(int,input().split())
value = list(map(int,input().split()))
total_value = sum(value)
if total_value  < t:
    print(0)
    sys.exit()
dp = []
for i in range(n+1):
    dp.append([0] + [-float("inf")]*(total_value))
for i in range(1,n+1):
    for j in range(1,total_value+1):
        if value[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i - 1][j - value[i - 1]] + value[i - 1])
for k in range(t,total_value+1):
    if dp[n][k] > 0:
        print(dp[n][k])
        sys.exit()
print(0)
