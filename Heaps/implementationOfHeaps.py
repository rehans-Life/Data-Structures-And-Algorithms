# Implementation of a Max Heap
class Heap:
    def __init__(self) -> None:
        self.arr = []
    
    def insert(self,val: int) -> None:
        self.arr.append(val)
        i = len(self.arr) - 1
        if i != 0: self.shiftup(i)
        
    def shiftup(self,i: int) -> None:
        parent = (i-1) //  2
        while parent >= 0 and self.arr[parent] < self.arr[i]:
            self.arr[parent],self.arr[i] = self.arr[i],self.arr[parent] 
            i = parent
            parent = (i-1) // 2
    
    def delete(self):
        # If heap empty return None
        if not len(self.arr):
            return None        
        # Bringing the last node value to the root and then deleting the last node so the duplicate value
        # value is gone
        self.arr[0] = self.arr[len(self.arr)-1]
        val = self.arr.pop()
        # Then we need to bring the root value to its actual position.
        self.shiftdown()        
        return val
    
    def shiftdown(self,i=0):
        
        leftChild = 2*i + 1
        rightChild = 2*i + 2
        
        while (leftChild < len(self.arr) and self.arr[leftChild] > self.arr[i]) or (rightChild < len(self.arr) and self.arr[rightChild] > self.arr[i]):
            
            # Getting the greater childs index.
            greater = leftChild if rightChild >= len(self.arr) or self.arr[leftChild] > self.arr[rightChild] else rightChild
            
            # Swapping the ith element which its greater child
            self.arr[i],self.arr[greater] = self.arr[greater],self.arr[i]
            
            # Setting the ith element to its new index 
            i = greater
            
            # Calculating the indexes of the new children
            leftChild = 2*i + 1
            rightChild = 2*i + 2    
        
    def heapify(self,arr):
        
        self.arr = arr
        n = len(self.arr)
        
        # We are checking from the bottom most subtrees and then moving on to upper
        # subtrees and checking if they respect the heap property or not.
        for i in reversed(range(0,((n-1) // 2) + 1)):
            self.shiftdown(i)
         
    def __str__(self) -> str:
        return str(self.arr)
    
heap = Heap()
heap.heapify([-2, -9, -1, -3])
print(heap)
# heap.insert(20)
# heap.insert(30)
# heap.insert(44)
# heap.insert(25)
# heap.insert(54)
# heap.insert(52)
# print(heap)
# heap.delete()
# heap.delete()
# print(heap)
