'''
刘思瑞 2100017810
'''
n = int(input())
sum =0
for i in range(1,n+1):
    if i % 7 != 0 and not('7' in str(i) ):
        sum += i**2
print(sum)
