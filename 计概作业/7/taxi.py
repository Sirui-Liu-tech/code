'''
刘思瑞 2100017810
'''
sum = 0
a = [0]*4
n = int(input())
for i in map(int,input().split()):
    a[i-1] += 1
sum += a[3]+a[2]
if a[0] <= a[2]:
    a[0] = 0
else:
    a[0] -= a[2]
sum += a[1] // 2
a[1] = a[1]%2
if a[1]:
    sum+=1
    if a[0] <= 2:
        a[0] = 0
    else:
        a[0] -= 2
sum += a[0]//4
if a[0] %4:
    sum += 1
print(sum)