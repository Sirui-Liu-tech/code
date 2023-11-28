'''
刘思瑞 2100017810
'''
n = int(input())
li = list(map(int,input().split()))
num = 1
flag = True
for i in range(n-1):
    if li[i] !=li[i+1]:
        flag = li[i+1]>li[i]
        num=2
        break

for i in range(n-1):
    if li[i+1] == li[i]:
        continue
    if flag:
        if li[i+1] < li[i]:
            num+=1
            flag = not flag
    else:
        if li[i+1] > li[i]:
            num+=1
            flag = not flag

print(num)