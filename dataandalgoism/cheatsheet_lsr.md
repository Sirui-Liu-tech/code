# 数据结构与算法速查表

## 树的相关算法

### 二叉树遍历

#### 前序遍历 (Pre-order Traversal)
```python
def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
```

#### 中序遍历 (In-order Traversal)
```python
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)
```

#### 后序遍历 (Post-order Traversal)
```python
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)
```

#### 层序遍历 (Level-order Traversal)
```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### 二叉搜索树 (BST) 插入节点
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root
```

### 二叉搜索树 (BST) 查找节点
```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
```

## 经典的排列算法

以下是十大经典的排列算法，每种算法都有不同的用途和特点：

## 1. 冒泡排序 (Bubble Sort)
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

## 2. 选择排序 (Selection Sort)
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

## 3. 插入排序 (Insertion Sort)
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

## 4. 归并排序 (Merge Sort)
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
```

## 5. 快速排序 (Quick Sort)
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

## 6. 希尔排序 (Shell Sort)
```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```

## 7. 堆排序 (Heap Sort)
```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

## 8. 计数排序 (Counting Sort)
```python
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr
```

## 9. 基数排序 (Radix Sort)
```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
```

## 10. 桶排序 (Bucket Sort)
```python
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket = []
    slot_num = 10 
    for i in range(slot_num):
        bucket.append([])

    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)

    for i in range(slot_num):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr
```

这十种排序算法涵盖了从简单的冒泡排序到复杂的基数排序，每种算法都有其适用的场景和优缺点。根据具体应用场景选择合适的排序算法，可以提高程序的性能和效率。

## 图的相关算法

### 深度优先搜索 (DFS)
```python
def dfs(graph, start):
    visited = set()
    def _dfs(v):
        if v not in visited:
            print(v)
            visited.add(v)
            for neighbor in graph[v]:
                _dfs(neighbor)

    _dfs(start)
```

### 广度优先搜索 (BFS)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append(neighbor)
```

### Dijkstra算法 (单源最短路径)
```python
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {start: 0}
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        if current_dist > dist.get(current_vertex, float('inf')):
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            if distance < dist.get(neighbor, float('inf')):
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist
```

### 拓扑排序 (Topological Sorting)
```python
def topological_sort(graph):
    visited = set()
    stack = []

    def _topological_sort(v):
        if v not in visited:
            visited.add(v)
            for neighbor in graph[v]:
                _topological_sort(neighbor)
            stack.append(v)

    for vertex in graph:
        _topological_sort(vertex)

    return stack[::-1]
```

### Kruskal算法 (最小生成树)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    return mst
```

