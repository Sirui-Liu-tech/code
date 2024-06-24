'''
2100017810 刘思瑞
'''
from collections import defaultdict
n = int(input())
d = defaultdict(list)
e = {'M':1,'B':1000}
for i in range(n):
    name, attribute = input().split('-')
    d[name].append(attribute)
kkk = d.keys()
kkk = list(kkk)
kkk.sort()
for i in kkk:
    d[i].sort(key= lambda x: float(x[:-1])* e[x[-1:]])
    print(i+":",end=' ')
    for j in range(len(d[i])-1):
        print(d[i][j],end=', ')
    print(d[i][len(d[i])-1])