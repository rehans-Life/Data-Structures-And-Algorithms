# Optimal Approach

# Time Complexity: O(n)
# Space Compleixty: O(k) 
# --> Because our deques size is never going to exceed the elements within the window.

from collections import deque

def sumMinMaxOfK(arr,k):
    
    # In this variable im going to accumulate the sum of min and max elements 
    # of each subarray of size k
    result = 0
    
    # A deque which is going to consist of the minimum element of each
    # window in its start
    minDeque = deque()
    
    # A deque which is going to consist of the maximum element of each
    # window in its start
    maxDeque = deque()
    
    # Pointers to maintain and slide our window of size k.
    i,j = 0,0
    
    n = len(arr)
    
    while j < n:
        
        # We include our jth element in both the deques.
        
        # While inserting the jth element in the minDeque i should remove
        # all elements which are greater than it and are infront of it 
        # in thr deque cause they are never going to become our answers again
        while len(minDeque) > 0 and minDeque[len(minDeque)-1] > arr[j]:
            minDeque.pop()
            
        minDeque.append(arr[j])
        
        # While inserting the jth element in the maxDeque i should remove all
        # elements which are lesser than it and are infront of it in the queue
        # cause they are never going to become our maximum elements again for
        # any subarray.
        while len(maxDeque) > 0 and maxDeque[len(maxDeque)-1] < arr[j]:
            maxDeque.pop()
            
        maxDeque.append(arr[j])
        
        # Until window size hits we keep incrementing j
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            # When window size hits then basically the first element in minDeque
            # in the minimum element of this window
            # And the first element in our maxDeque in our maximum element of
            # this window
            # So we can find there sum and add it to our accumulator
            result+=(maxDeque[0]+minDeque[0])   
            
            # Move the window.
            # Before that i check if my ith element is in starting element 
            # of any of the deques if it is then we need to remove it from
            # the deques or else it has already been removed by the max
            # min elements in the window from the deque.
            
            # The reason as to why i need to remove it is because its not going
            # to be inside of any of my windows anymore.
            
            if maxDeque[0] == arr[i]:
                maxDeque.popleft()
                
            if minDeque[0] == arr[i]:
                minDeque.popleft()
            
            # Icrementing both index pointers to slide the window
            i+=1
            j+=1
             
    return result    
            
arr = [2,5,-1,7,-3,-1,-2]

print(sumMinMaxOfK(arr,4))