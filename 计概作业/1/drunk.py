"""
刘思瑞 2100017810
"""
def prison(t):
    n = 0
    for i in range(1,t+1):
        m = 0
        for j in range(1,i+1):
            if not(i%j):
                m = not(m)
        if m :
            n += 1
    return n   
a = []
for i in range(int(input())):
    a.append(prison(int(input())))
for i in a:
    print(i)