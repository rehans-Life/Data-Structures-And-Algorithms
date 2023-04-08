def shiftdown(heap,i):

    leftChild = 2*i+1
    rightChild = 2*i+2

    while (leftChild < len(heap) and heap[i] < heap[leftChild]) or (rightChild < len(heap) and heap[i] < heap[rightChild]):
        greater = leftChild if rightChild >= len(heap) or heap[leftChild] > heap[rightChild] else rightChild
        heap[i],heap[greater] = heap[greater],heap[i]
        i = greater
        leftChild = 2*i + 1
        rightChild = 2*i + 2       

def mergeHeap(arr1, arr2):
    
    heap = []
    
    for num in arr1: heap.append(num)
    for num in arr2: heap.append(num)

    n = len(heap)
    for i in reversed(range(n//2)): 
        shiftdown(heap,i)
    
    return heap
