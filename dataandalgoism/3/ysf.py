'''
2100017810 刘思瑞
'''
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class ysf(object):
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head:
            return False
        else:
            return True
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

while True:
    n,p,m = map(int,input().split())
    if (n,p,m) == (0,0,0):
        break
    ysfi = ysf()
    for i in range(1,n+1):
        ysfi.append(i)
    begin = ysfi.head
    if p !=1:
        for i in range(p-2):
            begin = begin.next
    else:
        for i in range(n-1):
            begin = begin.next
    for j in range(n-1):
        for i in range(m-1):
            begin = begin.next
        print(begin.next.item,end=',')
        begin.next = begin.next.next
    begin = begin.next
    print(begin.item)

