'''
刘思瑞 2100017810
'''
a,b=input().split()
a= int(a)
b= int(b)
c=0
l=[]
for i in range(a):
    l.append(float(input())*100)
    c+=l[i]
d = c//b
if c<b:
    print('0.00')
else:
    max=d
    min=0
    while max-min>1:
        p=0
        for i in l:
            p+=i//d
        if p>=b:
            min=d
            d = (max+d)//2
        elif p<b:
            max=d
            d=(d+min)//2
    p=0
    for i in l:
        p+=i//max

    if p>=b:
        d=max
    else:
        d=min
    e=d/100
    print("%.2f" % e)
