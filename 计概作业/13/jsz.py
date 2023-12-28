'''
刘思瑞 2100017810
'''
import bisect
n = int(input())
L = list(map(int,input().split()))
L.sort()
sum = 0
for i in range(n-1):
    sum += L[0] + L[1]
    bisect.insort(L,L[0]+L[1])
    L = L[2:]
print(sum)