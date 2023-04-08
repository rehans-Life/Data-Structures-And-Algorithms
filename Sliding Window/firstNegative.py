from collections import deque

def firstNegative(arr,k):    
    n = len(arr)

    # Two pointers which are going to point at the start and at the end of the window
    i,j=0,0
    
    # A Queue which is going to store the negative elements inside of a window
    
    # Im using a Queue because its provides efficient insertions and removal from the left side.
    window = deque()
    # Results which is going to store the 1st negative elements inside of every window.
    results = list()
    
    # Running a while loop that runs until there are no more windows that can be created
    while j < n:
        
        # The calculation here is that we include each negative element through which my j pointer is 
        # traversing through 
        
        # This is going to be used to find the first negative integer inside of each windows
        if arr[j] < 0:
            window.append(arr[j])
    
        # Until i hit my window size im going to incrementing j
        if (j-i+1) < k:
            j+=1
        elif (j-i+1) == k:
            
            # Finding the answer through the queue ive maintained
            
            # So basically this windows first negative integer is always going to be the first element
            # inside of the queue
            
            # But if the queue is empty hence there are no negative elements inside of this current window
            
            if len(window) == 0:
                results.append(0)
            else: 
                results.append(window[0])

                # Now when im going to slide my window my ith element is not going to be a part of that element
                # and hence if it is a negative element i need to remove it from my list since the list should 
                # only contain negative elements inside of the current window hence i need to remove ith element
                # since its not going to a part of the next window
                
                # Since ith element points at the first element inside of the array and we know if its negative
                # then its going to be the first negative integer of the window so i can just remove the first
                # element of my queue to remove it.
                if arr[i] < 0:
                    window.popleft()
            
            # Moving the pointers to the new window.
            i+=1
            j+=1
    
    return results

print(firstNegative([-2,-1,-5,-6,-2,-1,-6],2))