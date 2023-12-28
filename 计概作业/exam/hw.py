'''
2100017810 刘思瑞
'''
H,L,n = map(int,input().split())
velosity = list(map(int,input().split()))
velosity.sort()
vmax = velosity[n//2]
print(f"{H-0.5*10*((L/vmax)**2):.2f}")

