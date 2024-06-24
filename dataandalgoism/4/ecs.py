'''
2100017810 刘思瑞
'''
leng = []
def search(tree,lens,start):
    global leng
    if start == -2:
        leng.append(lens)
        return
    for i in tree[start]:
        search(tree,lens+1,i)
    return

tree = []
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    tree.append([a-1,b-1])
search(tree,0,0)
print(max(leng))