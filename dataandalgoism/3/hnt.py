'''
2100017810 刘思瑞
'''

num,a,b,c = input().split()
num =int(num)
pin = [a,b,c]
def outputt(n,a,b):
    global pin
    print('%d:%s->%s' %(n,pin[a],pin[b]))
def secp(a,b):
    m = [0,1,2]
    m.remove(a)
    m.remove(b)
    return m[0]
    
def move(num,a,b):
    if num == 0:
        return
    move(num-1,a,secp(a,b))
    outputt(num,a,b)
    move(num-1,secp(a,b),b)
    return

move(num,0,2)
