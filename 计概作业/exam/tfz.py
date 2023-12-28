'''
2100017810 刘思瑞
'''
n = int(input())
s = bin(n)[2:]
if s == s[::-1]:
    print('Yes')
else:
    print('No')