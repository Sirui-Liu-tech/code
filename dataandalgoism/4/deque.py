'''
2100017810 刘思瑞
'''
from queue import deque

def imple(a,b):
    global d
    if a ==1:
        d.append(b)
    else:
        if b:
            d.pop()
        else:
            d.popleft()

n = int(input())
for i in range(n):
    num = int(input())
    d  = deque()
    for j in range(num):
        a,b = map(int,input().split())
        imple(a,b)
    if d:
        for i in d:
            print(i,end=' ')
    else:
        print('NULL',end=' ')
    print()

    