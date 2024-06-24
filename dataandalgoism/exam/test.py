class treenode:
    def __init__(self,value):
        self.value = value
        self.chi = []

s = input()
stack = []
for i in s:
    if i =='(':
        stack.append(node)
    elif i == ')':
        node = stack.pop()
    elif i == ',':
        continue
    else:
        node = treenode(i)
        if stack:
            stack[-1].chi.append(node)
def preorder(node):
    output = [node.value]
    for child in node.children:
        output.extend(preorder(child))
    return ''.join(output)
def postorder(node):
    output = []
    for child in node.children:
        output.extend(postorder(child))
    output.append(node.value)
    return ''.join(output)

print(preorder(node))
print(postorder(node))