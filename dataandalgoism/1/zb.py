'''
2100017180 刘思瑞
'''
import collections
d = collections.defaultdict(int)
for i in list(map(int,input().split())):
    d[i] += 1
result= []
maxx = max(d.values())
for k,v in d.items():
    if v == maxx:
        result.append(k)
result.sort()
for i in result:
    print(i,end=' ')