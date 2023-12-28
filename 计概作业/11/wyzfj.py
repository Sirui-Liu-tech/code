'''
刘思瑞 2100017810
'''
n,k,crow,large,small,flag,temp = 0,0,[],0,0,False,0
def echo(d):
    global n,k,crow,large,small,flag,temp
    if d ==0:
        return
    if d==1:
        if temp:
            temp -= 1
            return
        else:
            if large:
                large,small = large-1,small+1
                return
            elif small:
                small-=1
                return
        flag = False
        return
    if d ==2:
        if small:
            small -= 1
            return
        else:
            if temp>=2:
                temp-=2
                return
            if large:
                if temp:
                    large -=1
                    small+=1
                    temp -=1
                    return
                else:
                    large,temp = large-1,temp+1
                    return
            if temp>=2:
                temp-=2
                return
        flag = False
        return
    if d ==3:
        if large:
            large -= 1
            return
        else:
            if temp:
                if small:
                    temp -=1
                    small-=1
                    return
            else:
                if small:
                    if large:
                        small-=1
                        large-=1
                        temp+=1
                    elif small>=2:
                        small-=2
                        return
        flag = False
        return
    if d == 4:
        if large:
            large -= 1
            return
        else:
            if small>=2:
                small-=2
                return
            else:
                if small:
                    if temp>=2:
                        small-=1
                        temp-=2
                        return
                elif temp>=4:
                    temp-=4
                    return
        flag = False
        return
    
def define(c):
    global n,k,crow,large,small,flag,temp
    for i in range(k):
        rest = crow[i]//4
        for j in range(rest):
            echo(4)
        echo(crow[i]%4)
        if not flag:
            return 'NO'
    return 'YES'
            
n,k = map(int,input().split())
crow = list(map(int,input().split()))
small = 2*n
large = n
temp = 0
flag = True
crow.sort()
print(define(1))