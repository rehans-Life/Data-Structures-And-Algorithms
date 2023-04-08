from typing import List
from heapq import heapify,heappop,heappush

def kClosest(nums: List[int],x: int,k : int):
    # A maxHeap which is going to store upto k elements inside of it with the lowest difference to x
    heap  = []
    heapify(heap)
    
    for num in nums:
        # Im going to insert each element into the heap along with its difference with x cause the heap is going
        # to be sorted on its basis
        heappush(heap,[-1 * abs(x-num),num])
        
        # If the length of the heap has become k+1 hence then the root node has higher difference with x then 
        # k other elements then that means it cannot be our answer so we pop it
        if len(heap) == k+1:
            heappop(heap)
        
    return [num for diff,num in heap]
            
print(kClosest([5,6,7,8,9],7,3))