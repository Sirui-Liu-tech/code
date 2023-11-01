'''
刘思瑞 2100017810
'''
sum = 0
n = int(input())
l = list(map(int,input().split()))
l.sort()
for i in l:
    if i >= sum:
        sum += i
    else:
        n -= 1
print(n)