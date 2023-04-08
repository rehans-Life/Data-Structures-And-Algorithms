    # For any index i its acutal element lies with in the range i-k and i+k indexes
    # elements

    # Approach would be to traverse from left to right indexes and each index i look
    # at elements till i+k and find the smallest one and place it there.

    # Why only i+k cause when i = 0 then there is no behind then when im at this 
    # index im going to find the correct element to place there from i+k.

    # Then when im at index 1 i know at index 0 we have the correct element there
    # so we wont look behind and only look at 1+k indexes elements then find the
    # right element to place there.

    # Then at index 2 i already have correct elements at index 0 and 1 so ill not
    # look behind and only look at 2+k elements cause there the element of interest
    # could lie

    # And since im going from left to right indexes i will always find the smallest
    # element to place at any index i.
    
    # Now how do we find the most efficient way to find the smallest element
    # from the left of any index i.

import heapq

def nearlySorted(arr, k):

    heap = []
    heapq.heapify(heap)
    i = 0

    for j in range(len(arr)):

        heapq.heappush(heap,arr[j])

        if len(heap) > k:
            arr[i] = heapq.heappop(heap)
            i+=1
    
    while i < len(arr):
        arr[i] = heapq.heappop(heap)
        i+=1

    return arr

