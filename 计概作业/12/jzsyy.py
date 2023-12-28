'''
2100017810 刘思瑞
'''
def value(buynumber):
    global boutique,maion
    boutiquevalue = [0]*m
    for i in range(n):
        boutiquevalue[buynumber[i]]+=(boutique[i][buynumber[i]])
    minusvalue = 0
    for i in range(m):
        summ = 0
        if boutiquevalue[i] != 0:
            for j in maion[i]:
                if j[1] > summ and j[0] <= boutiquevalue[i]:
                    summ = j[1]
        minusvalue += summ
    return sum(boutiquevalue) - (50*(sum(boutiquevalue)//300)) - minusvalue
def bianli(i,buynumber):
    global minn
    if i == n:
        minn = min(minn,value(buynumber))
        return
    for j in range(m):
        buynumber.append(j)
        bianli(i+1,buynumber)
        buynumber.pop()
    return
    
n,m = map(int,input().split())
boutique = []
maion = []
for i in range(n):
    part = list(input().split())
    _ = [10**6] * m
    for x in part:
        _[list(map(int,x.split(':')))[0]-1]= list(map(int,x.split(':')))[-1]
    boutique.append(_)
for i in range(m):
    part = list(input().split())
    _ = [list(map(int,x.split('-'))) for x in part]
    maion.append(_)
minn = value([0]*n)
bianli(0,[])
print(minn)