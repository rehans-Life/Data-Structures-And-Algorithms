from collections import deque

# Ive been given an array nums and an integer k and i need to find
# the maximum value of each window of size k and store it in an array.
def slidingWindowMax(nums,k):
    n = len(nums)
    # Initializing pointers for the window.
    i,j = 0,0
    
    # A deque which is going to store the elements that j pointer is 
    # traversing through.
    window = deque()
    
    # A results array which is going to store the maximum values
    # of each window.
    results = list()
    
    while j < n:
        # So the element to which my j pointer is pointing at in the
        # array 
        
        # I need to start checking from the right that by how many 
        # elements it is greater and im going to accordingly start
        # remove those elements that this element is greater by.
        while len(window) > 0 and window[len(window)-1] < nums[j]:
            window.pop()
        
        # I append it after removing all the elements smaller than it
        # from it from the queue    
        window.append(nums[j])
        
        # Im going to keep incrementing j until window size hits k
        if (j-i+1) < k:
            j+=1
        elif (j-i+1) == k:
            # The maximum element of this window be the first element in the 
            # queue
            results.append(window[0])

            # Sliding the window
            
            # So basically before sliding the window i know my current ith
            # element isnt going to be inside of my window so i need to undo
            # the changes which j made when it traversed through the current
            # ith element 
            
            # So basically if the ith element isnt the maximum element then 
            # that means the maximum is on its right then that means i have
            # already removed from the window because ive found an element
            # which was greater than this element in my window so the changes
            # have already been undone when ive found an element greater than 
            # this element in my window.
            
            # But if my ith element is pointing at the max element of the 
            # window then i remove it from the queue cause its not going to
            # be in the new window.
            if nums[i] == window[0]:
                window.popleft()
                
            j+=1
            i+=1
        
    return results    
    
    
    
    