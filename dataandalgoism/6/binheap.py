'''
刘思瑞 2100017810
'''
class Binheap:
    def __init__(self):
        self.hList = [0]
        self.size = 0
    def rollup(self,i):
        while i // 2 > 0:
            if self.hList[i] < self.hList[i // 2]:
                self.hList[i // 2], self.hList[i] = self.hList[i],self.hList[i // 2]
            i = i // 2
    def insert(self,value):
        self.hList.append(value)
        self.size += 1
        self.rollup(self.size)
    def rolldown(self,i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.hList[i] > self.hList[mc]:
                self.hList[i],self.hList[mc] = self.hList[mc],self.hList[i]
            i = mc
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.hList[i * 2] < self.hList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):
        retval = self.hList[1]
        self.hList[1] = self.hList[self.size]
        self.size = self.size - 1
        self.hList.pop()
        self.rolldown(1)
        return retval
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.hList = [0] + alist[:]
        while (i > 0):
            self.rolldown(i)
            i = i - 1


n = int(input())
m = Binheap()
for i in range(n):
    s = input()
    if s[0] =='1':
        m.insert(int(s[2:]))
    else:
        print(m.delMin())

