'''
刘思瑞 2100017810
'''
import sys
N = int(input())
S = list(map(int,input().split()))
num  = len(S)
def dfs(N,S,i):
    if N == 1:
        print('YES')
        sys.exit()
    for j in range(i+1,num):
        if N%S[j] ==0:
            dfs(N//S[j],S,j)
    return
if N ==1:
    if 1 in S:
        print('YES')
    else:
        print('NO')
else:
    dfs(N,S,-1)
    print('NO')