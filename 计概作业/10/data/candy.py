'''
刘思瑞 2100017810
'''
def count(i,j,k):
    maxx = max(i,j)
    minn = min(i,j)
    if k:
        if maxx > minn:
            maxx-=1
            minn+=1
    return minn*(minn+1)//2+(maxx+1)*(maxx+2)//2 -1

num = int(input())
li = []
li += list(map(int,input().split()))
li.append(-1)
flag = True
upnum =-1
downnum =1
equal =False
sum = 0
for i in range(num):
    if flag:
        if li[i]<li[i-1]:
            flag = not flag
        elif li[i] == li[i-1]:
            if li[i] == li[i+1]:
                sum+=1
                continue
            flag = not flag
            equal = True
        else:
            upnum += 1
    else:
        if li[i]>li[i-1]:
            flag = not flag
            sum += count(upnum,downnum,equal)
            equal = False
            upnum = 1
            downnum =1
        elif li[i] == li[i-1]:
            if li[i] == li[i+1]:
                sum+=1
                continue
            flag = not flag
            sum += count(upnum,downnum,equal)
            equal = False
            upnum = 0
            sum+= 1
            downnum =1
        else:
            downnum += 1
if flag:
    sum += count(upnum,0,equal)
else:
    sum += count(upnum,downnum,equal)
print(sum+1)
