'''
刘思瑞 2100017810
'''
s = input()
re = ['a','e','i','o','u','y']
s = s.lower()
for i in re:
    s = s.replace(i,'')
for i in s:
    print('.'+ i,end = '')