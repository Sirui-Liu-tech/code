'''
刘思瑞 2100017810
'''
def culcu(t):
    global long
    m0 , d0 , ini , m ,d = map(int,input().split())
    day = 0
    if m0 == m:
        times = d - d0
    else:
        for i in range(m0+1,m):
            day += long[i]
        times = long[m0] - d0 +day+d
    return ini * (2 ** times)

long = [0 , 31,28,31,30,31,30,31,31,30,31,30,31]
n = int(input())
for i in range(n):
    print(culcu(1))
