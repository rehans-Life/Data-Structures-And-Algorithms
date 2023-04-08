import heapq

# Since Im traversing the array hence thats going to take O(n) time then for each element we
# traverse we are taking logk time to insert cause the height of the binary heap never exceeds k

# Therefore Time Complexity is: O(nlogk)
# And Space Complexity is: O(k) => For the Heap itself.

def kthSmallest(arr, k):

    # Creating a heap structure
    heap = []
    heapq.heapify(heap)

    # Traversing the array from left to right
    for num in arr:

        # Pushing each element we traverse into the heap
        heapq.heappush(heap,-1 * num)

        # If after inserting the new element if the size of the heap has exceeded
        # k then that means the top most node is cannot be my answer cause its 
        # greater than k elements therefore it cannot be the kth smallest element
        # anymore so i remove it from the stack
        
        if len(heap) > k: heapq.heappop(heap)

    # Since to use the minHeap as a maxHeap i had to mulyiply the elements im inserting by -1
    # therefore i multiply the number by -1 again to convert it into its original form.
    return heap[0] * -1
