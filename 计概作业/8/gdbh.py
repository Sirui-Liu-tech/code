'''
刘思瑞 2100017810
'''
def su(i):
    for j in range(2,int(i**0.5)+2):
        if i%j == 0:
            return False
    return True
def find(n):
    if n < 6 or n % 2 != 0 :
        print('Error!')
        return 
    for i in range(3,n//2 +1 ,2):
        if su(i):
            if su(n-i):
                print(str(n)+ '=' + str(i) + '+' + str(n-i))
    return
n = int(input())
find(n)
