def pickToys(s: str):
    
    # So basically bhar ma jai question statement just find the longest 
    # substring with 2 unique elements.
    
    # Two pointers for the start and the end of the window.
    i,j =0,0
    
    # A map to store all the unique elements from a subString.
    unique = dict()
    
    # A variable which is going to store longest substring length with 
    # only two unique elements.
    maxToys = 0
    
    n = len(s)
    
    while j < n:
        
        # Im going to add the elements j is traversing inside of the map 
        # if it already exists i increment it if it doesnt i add and set it
        # to 1.
        if s[j] not in unique:
            unique[s[j]] = 1
        else:
            unique[s[j]]+=1         
        
        if len(unique) == 2:
            maxToys = max(maxToys,(j-i+1))
            j+=1
        # Keep incrementing j until there are exactly two unique elements inside of it.
        elif len(unique) < 2:
            j+=1
        else:
            # We keep incrementing i pointer until our window hits the condition hits the condition.
            while len(unique) > 2:
                unique[s[i]]-=1
                if unique[s[i]] == 0:
                    del unique[s[i]]
                i+=1
            j+=1
    
    return maxToys
            
print(pickToys('abaccab'))