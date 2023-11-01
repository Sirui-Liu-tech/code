'''
刘思瑞 2100017810
'''
plate = []
n,m = 0,0
def inplem(r,c,p,f):
    global plate,n,m
    p = (p-1)//2
    rmin = max(0,r-p)
    cmin = max(0,c-p)
    rmax = min(n-1,r+p)
    cmax = min(m-1, c+p)
    if f == 0:
        for i in range(rmin,rmax+1):
            for j in range(cmin,cmax+1):
                plate[i][j] = False
    else:
        pllaa = []
        for i in range(n):
            pllaa.append([False]*m)
        for i in range(rmin,rmax+1):
            for j in range(cmin,cmax+1):
                pllaa[i][j] = plate[i][j]
        plate = pllaa
    
n , m , k = map(int,input().split())
plate = []
for i in range(n):
    plate.append([True]*m)
for i in range(k):
    r,c,p,f = map(int,input().split())
    inplem(r-1,c-1,p,f)
sum = 0
for i in plate:
    for j in i:
        if j:
            sum += 1
print(sum)