'''
刘思瑞 2100017810
'''
f = [1 ,1 ,2]

def forward(t):
    global f
    f = f[1:]
    f.append(f[0]+f[1])

n = int(input())
for i in range(n):
    a = int(input())
    f = [1 ,1 ,2]
    if a <= 3:
        print(f[a-1])
    else:
        for j in range(a-3):
            forward(1)
        print(f[2])