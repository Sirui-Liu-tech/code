'''
刘思瑞 2100017810
'''
n = int(input())
for i in range(n):
    if 360 % (180 - int(input())) == 0:
        print('YES')
    else:
        print('NO')