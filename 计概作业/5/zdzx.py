'''
刘思瑞 2100017810
'''
#冒泡排序
def compare(s1,s2):
    if int(s1 + s2) > int(s2 +s1):
        return True
    else:
        return False  
n = int(input())
number = list(input().split())
#max number:
for i in range(n-1):
    for j in range(i+1,n):
        if not compare(number[i],number[j]):
            temp = number[j]
            number[j] = number[i]
            number[i] =temp
for i in number:
    print(i,end='')
print(' ',end='')
#min number:
number.reverse()
for i in number:
    print(i,end='')