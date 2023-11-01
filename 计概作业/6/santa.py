'''
刘思瑞 2100017810
'''
n , w0 = map(int,input().split())
record = []
for i in range(n):
    v , w = map(int,input().split())
    record.append([v/w,v,w])
for i in range(n-1):
    for j in range(n-1-i):
        if record[j][0] < record[j+1][0]:
            record[j] , record[j+1] = record[j+1] , record[j]
sum = 0
for i in record:
    if i[2] < w0:
        sum+= i[1]
        w0 -= i[2]
    else:
        sum+= i[0] * w0
        break
print('%.1f' % sum)