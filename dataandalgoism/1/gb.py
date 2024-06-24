'''
2100017180 刘思瑞
'''
N = int(input())
isprime =[False] + [True for i in range(N+1)]
prime= []
def euler():
    global N
    isprime[1]=False
    for i in range(2,N) :
        if isprime[i]:
            prime.append(i)
        for j in prime:
            if i*j>=N:
                break
            isprime[i*j] = False
            if i%j == 0:
                break
euler()
for i in range(N):
    if isprime[i] and isprime[N-i]:
        print(i,N-i)
        break
