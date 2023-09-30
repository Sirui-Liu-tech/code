'''
刘思瑞 2100017810
'''
element = list(map(int,input().split('+')))
element.sort()
m = element[-1]
del element[-1]
for i in element:
    print(i,end='+')
print(m)
