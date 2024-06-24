'''
2100017810 刘思瑞
'''
class treenode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def decide(node):
    if node.left:
        if node.right.value == node.left.value:
            return node.right.value
        else:
            return 'F'

def build(N,l):
    if N == 0:
        return treenode(['B','I'][l[0]])
    o = treenode(0)
    ll = l[:2**(N-1)]
    lr = l[2**(N-1):]
    o.left = build(N-1,ll)
    o.right = build(N-1,lr)
    o.value = decide(o)
    return o

def postorder(tree):
    if tree != None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.value,end='')


N = int(input())
s = list(map(int,list(input())))
postorder(build(N,s))