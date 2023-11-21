'''
刘思瑞 2100017810
'''
max = 0
s = list(input().split('+'))
for i in s:
    j = list(i.split('n^'))
    if j[0] != '0':
        if int(j[1]) > max:
            max = int(j[1])
print('n^'+str(max)) 