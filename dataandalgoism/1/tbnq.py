'''
2100017180 刘思瑞
'''
n = int(input())
a,b,c = 0,1,1
for i in range(n-2):
    a,b,c = b,c,a+b+c
print(c)