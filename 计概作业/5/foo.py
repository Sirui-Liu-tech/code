'''
刘思瑞 2100017810
'''
import re

s = input()
if re.search('1{7}',s) or re.search('0{7}',s):
    print('YES')
else:
    print('NO')