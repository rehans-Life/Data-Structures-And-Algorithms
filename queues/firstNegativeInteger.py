#User function Template for python3
from collections import deque

def printFirstNegativeInteger( A, N, K):
    
    # A queue to store the negative elements inside of our
    # current window in order
    queue = deque()
    
    # Two pointers to denote our start and end of our window
    i = 0
    j = 0
    
    # an array to store the negative numbers for each window
    results = list()
    
    while j < N:
        
        # If j index pointer traverses through a negaitve
        # element we add it to the array.
        if A[j] < 0:
            queue.append(A[j])
        
        # Keep incrementing j pointer until window size hits
        if j-i+1 < K:
            j+=1
        elif j-i+1 == K:
            # When window size hits then current windows
            # first negative number is the first element
            # inside of our queue or if queue is empty
            # then there is no negative number in this 
            # current window
            if len(queue) == 0:
                results.append(0)
            else:
                results.append(queue[0])
            
            # Then move window by incrementing i and j 
            # and before that undoing the changes made for i
            
            # If ith element is negative then pop first number
            # from queue cause its not going to be inside of the
            # new window.
            if A[i] < 0:
                queue.popleft()
            
            i+=1
            j+=1
            
    return results