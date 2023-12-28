'''
2100017810 刘思瑞
'''
n = int(input())
l = list(map(int,input().split()))
l.sort()
for i in range(len(l)):
    if l[i] > n:
        break
l1 = l[:i]
l2 = l[i:]
for i in range(1,n+1):
    if i not in l1:
        print(i,end=' ')
print()
for i in l2:
    print(i,end=' ')
