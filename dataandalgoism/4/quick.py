def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr , 0
    middle = math.floor(len(arr)/2)
    left, inv_left = mergeSort(arr[:middle])
    right, inv_right = mergeSort(arr[middle:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge
def merge(left,right):
    result = []
    count = 0
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result += left[i:]
    result += right[j:]

    return result, count

while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    __, times = mergeSort(arr)
    print(times)