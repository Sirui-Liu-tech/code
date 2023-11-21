'''
刘思瑞 2100017810
'''

n , m = map(int,input().split())
store = [0]*m
totalyouhui = 0
for i in range(n):
    inde , price = map(int,input().split())
    store[inde - 1] += price
for i in range(m):
    manjian , youhui = map(int,input().split('-'))
    if store[i] >= manjian:
        totalyouhui += youhui
totalyouhui += ((sum(store))//200)*30
print(sum(store)-totalyouhui)