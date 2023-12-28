'''
刘思瑞 2100017810
'''
s = list(input().split())
w,dw = input().split()
w = w.lower()
dw = dw.lower()
sw =[w,w+',',w+'.',':'+w]
sdw =[dw,dw+',',dw+'.',':'+dw]
for i in range(len(s)):
    s[i] =s[i].lower()
    if s[i] in sw:
        s[i] = sdw[sw.index(s[i])]
s[0] = s[0][:1].upper() + s[0][1:]
for i in range(len(s)-1):
    if '.' in s[i]:
        s[i+1] = s[i+1][:1].upper() + s[i+1][1:]
for i in s:
    print(i,end=' ')
