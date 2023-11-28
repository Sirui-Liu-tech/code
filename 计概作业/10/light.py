'''
2100017810 刘思瑞
'''
def find(n,li,long,number):
    for i in range(min(0,long//2-1),num):
        if i-li[i] <= n and i+li[i] >= n:
            if i+li[i] > long:
                long = i + li[i]
    number+=1
    return long,li,long,number
num = int(input())
number = 0
li = list(map(int,input().split()))
long = 0
long, li,long,number = find(0,li,long,number)
while True:
    if long>=num-1:
        break
    long, li,long,number = find(long+1,li,long,number)
print(number)