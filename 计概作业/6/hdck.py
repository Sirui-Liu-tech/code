'''
刘思瑞 2100017810
'''
import queue
def maxx(q):
    global k
    maxu = q.get()
    q.put(maxu)
    for i in range(1,k):
        temp = q.get()
        q.put(temp)
        maxu = max(maxu,temp)
    return maxu

n , k = map(int,input().split())
queuee = list(map(int,input().split()))
q=queue.Queue()
for i in range(k):
    q.put(queuee[i])
print(maxx(q),end=' ')
for i in range(k,n):
    q.put(queuee[i])
    q.get()
    print(maxx(q),end=' ')