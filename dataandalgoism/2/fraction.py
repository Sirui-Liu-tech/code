'''
2100017810 刘思瑞
'''
import math

class fraction:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self,m):
        c = self.b * m.b
        d = self.a * m.b + self.b *m.a
        e = math.gcd(c,d)
        f = c//e
        g = d//e
        return fraction(g,f)
    def output(self):
        print('%d/%d' %(self.a ,self.b))

a,b,c,d = map(int,input().split())
p = fraction(a,b)
q= fraction(c,d)
(p.add(q)).output()

    