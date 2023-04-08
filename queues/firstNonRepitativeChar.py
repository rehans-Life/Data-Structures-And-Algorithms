from collections import deque

def firstNonRepeating(A: str):
    
    # A string to store the non repeating characters of each
    # input stream.
    ans = ""
    
    # Maintaining a hashmap to store the frequency of characters
    # in our current input stream
    count = dict()
    
    # A deque in which we are going to store our non repeating
    # elements of our currrent input stream and if we find
    # any repeating any elements we remove them from it 
    # In here the first character is supposed to be the first
    # non repeating char of the string if repeating we remove it 
    # from the front and land on the next non repeating character
    # in the input stream and thats why we need a hashmap to
    # store the frequency of characters.
    queue = deque()
    
    # Iterating through our input stream
    
    for char in A:
        
        # If the characrer we are inserting into our stream
        # is not already in the hashmap we add it or if its
        # already there we increment it.
        if char not in count:
            count[char] = 0
            
        count[char]+=1
        
        # We need to add the element to the end of the queue
        queue.append(char)
        
        # Then we need to find the first non repeating character
        # of our current input stream.
        
        # It should be the first character of our queue but it
        # could be due insertion it insnt the non repeating 
        # anymore so we need to remove it and get the next
        # non repeating element in order
        
        # for this we use hashmap 
        
        # It could also happen we keep removing elements as 
        # all are repeating and our queue goes empty in that
        # case there is no non repeating character in the current
        # input stream.
        
        while len(queue):
            # We remove elements from the start if there frequency
            # is greater than 1 cause then there not unique
            if count[queue[0]] > 1:
                queue.popleft()
            # If its not greater than 1 we stop cause thats our
            # answer we append that character as our answer and
            # break the loop
            else:
                ans+=queue[0]
                break
        
        # We couldve ended cause queue became empty then we
        # need to add a hash for this input stream in our answer
        if not len(queue):
            ans+='#'
        
    
    return ans
        
print(firstNonRepeating('oaoalalabonjbur'))     
        
        
        
        
    