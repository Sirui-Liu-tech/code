'''
刘思瑞 2100017810
'''
class treenode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insertTree(value,node):
    if node == None:
        return treenode(value)
    if node.value < value:
        node.right = insertTree(value,node.right)
    if node.value > value:
        node.left = insertTree(value,node.left)
    return node

def levelorder(tree):
    output = [tree]
    pri = [str(tree.value)]
    while output:
        ii = output.pop(0)
        if ii.left:
            output.append(ii.left)
            pri.append(str(ii.left.value))
        if ii.right:
            output.append(ii.right)
            pri.append(str(ii.right.value))
    print(' '.join(pri))

li = list(map(int,input().split()))
root = None
for i in li:
    root = insertTree(i,root)
levelorder(root)

