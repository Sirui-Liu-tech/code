'''
2100017810 刘思瑞
'''
N=10001
isprime = [True for i in range(N)]
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

def calcu(grade):
    global isprime
    temp = []
    for i in grade:
        if i == int(i**0.5)**2:
            if isprime[int(i**0.5)]:
                temp.append(i)
    if temp == []:
        print('0')
        return
    print('%.2f' % (sum(temp)/len(grade)))
    return

euler()
m , n = map(int , input().split())
for i in range(m):
    calcu(list(map(int , input().split())))