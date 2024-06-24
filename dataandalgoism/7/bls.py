'''
2100017810 刘思瑞
'''
class treenode():
    def __init__(self,value,child):
        self.value = value
        self.child = child

def sortorder(tree):
    global hasvis,node
    while True:
        if tree != None:
            temp = []
            for i in [tree.value]+tree.child:
                if i not in hasvis:
                    temp.append(i)
            if not temp :
                return
            m = min(temp)
            print(m)
            hasvis.add(m)
            sortorder(node[m])


n = int(input())
node = dict()
for i in range(n):
    s = list(map(int,input().split()))
    v,l = s[0],s[1:]
    node[v] = treenode(v,l)
    if i == 0:
        origin  = node[v]
while True:
    temp = origin
    for i in node.values():
        if origin.value in i.child:
            origin = i
    if origin == temp:
        break
hasvis = set()
sortorder(origin)