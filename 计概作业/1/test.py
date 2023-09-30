'''
刘思瑞 2100017810
'''
def exchange(t):
    global d, num
    if t.head:
        list1 = [t.head.data]
        temp = t.head
        minnum = t.head.data - d
        maxnum = t.head.data + d
        while True:
            try:
                if temp.data - d > minnum:
                    minnum = temp.data -d
                if temp.data + d < maxnum:
                    maxnum = temp.data + d
                if maxnum < minnum:
                    break
                if (temp.next.data >= minnum) and (temp.next.data <= maxnum):
                    list1.append(temp.next.data)
                    if temp.next.data - d > minnum:
                        minnum = temp.next.data -d
                    if temp.next.data + d < maxnum:
                        maxnum = temp.next.data + d
                    if maxnum < minnum:
                        break
                    temp.delete_by_element()
                else:
                    temp = temp.next
            except AttributeError:
                break
        t.head = t.head.next
        return  list1
    else:
        return  None

class LNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def delete_by_element(self):
        if self.next.next:
            self.next = self.next.next
        else:
            self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = LNode(data[0])
        p = self.head
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next

    def delete(self, index):
        q = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                q = q.next
            r = q
            if (r.next).next:
                q.next = r.next.next

num , d = map(int, input().split())
hight = []
for i in range(num):
    hight.append(int(input()))
height = LinkList()
height.initList(hight)
list_temp = [1]
while list_temp:
    list_temp = exchange(height)
    if not list_temp:
        break
    list_temp.sort()
    for j in list_temp:
        print(j)
