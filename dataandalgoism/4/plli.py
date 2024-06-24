'''
2100017810 刘思瑞
'''
from queue import deque
def calcu():
    global m,n
    a = m.pop()
    if a in ('+','-','*','/'):
        b = n.pop()
        c = n.pop()
        n.append(str(eval(b+a+c)))
    else:
        n.append(a)

s = list(input().split())
m = deque(s)
n = deque()
while True:
    calcu()
    if not m:
        break
print('%.6f' %float(n[0]))
