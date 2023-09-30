'''
刘思瑞 2100017810
'''
x = 0
n = int(input())
for i in range(n):
    if input()[1] == '+':
        x += 1
    else:
        x -= 1
print(x)