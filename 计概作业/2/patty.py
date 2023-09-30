'''
刘思瑞 2100017810
'''
s1 = input()
s2 = input()
l = len(s1)
j = 0
for i in range(l):
    m = ord(s1[i]) 
    n = ord(s2[i]) 
    if m >= 97 and m <= 122:
        m -= 32
    if n >= 97 and n <= 122:
        n -= 32
    if m > n:
        j = 1
        break
    elif m < n:
        j = -1
        break

print(j)
        