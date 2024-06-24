'''
刘思瑞 2100017810
'''
class treenode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def buildTree(preorder):
    if len(preorder) == 0:
        return None
    node = treenode(preorder[0])
    num = len(preorder)
    for i in range(1, len(preorder)):
        if preorder[i] > preorder[0]:
            num = i
            break
    node.left = buildTree(preorder[1:num])
    node.right = buildTree(preorder[num:])
    return node

def postorder(tree):
    if tree != None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.value,end=' ')

n = int(input())
li = list(map(int,input().split()))
root = buildTree(li)
postorder(root)

