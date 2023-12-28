'''
刘思瑞 2100017810
'''
n=int(input())
l=list(map(int,input().split()))
a,b=[0]*(10**6),[0]*(10**6)
ans=1
j=1
for i in range(0,n):
    a[l[i]]+=1
    b[a[l[i]]]+=1
    if a[l[i]]*b[a[l[i]]]==j and j!=n:
        ans=j+1
    elif a[l[i]]*b[a[l[i]]]==j-1:
        ans=j
    j+=1
print(ans)