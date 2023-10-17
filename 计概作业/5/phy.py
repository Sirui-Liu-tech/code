'''
刘思瑞 2100017810
'''
n = int(input())
sum = [0,0,0]
for i in range(n):
    li = list(map(int,input().split()))
    for j in range(3):
        sum[j] += li[j]
if sum == [0]*3:
    print('YES')
else:
    print('NO')