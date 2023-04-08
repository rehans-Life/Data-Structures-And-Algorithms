def shiftdown(arr,i,n):    
    leftChild = 2*i + 1
    rightChild = 2*i + 2
    
    while(leftChild < n and  arr[leftChild] > arr[i]) or (rightChild < n and arr[rightChild] > arr[i]):
        smaller = leftChild if rightChild >= n or arr[leftChild] > arr[rightChild] else rightChild
        arr[i],arr[smaller] = arr[smaller],arr[i]
        i = smaller
        leftChild,rightChild = 2*i+1,2*i+2

def heapify(arr): 
    for i in reversed(range(len(arr)-1//2 + 1)): shiftdown(arr,i,len(arr))

def delete(arr):
    arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    val = arr.pop()
    shiftdown(arr,0)
    return val

def heapsort(arr):
    
    heapify(arr)
    
    for i in reversed(range(len(arr))): 
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr)     
        
    return arr

arr = [34,23,29,34,2,2,1,2,3,53,21,56]
print(heapsort(arr))


