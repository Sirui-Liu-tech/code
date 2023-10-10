'''
刘思瑞 2100017810
'''
def detect(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

num = int(input())
for i in range(num//2,num-1):
    if detect(i) and detect(num - i):
        print(i*(num-i))
        break
