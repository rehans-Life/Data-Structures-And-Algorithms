def nextAlphabet(arr,n,alphabet):
    
    # Setting up two pointers to denote the range im searching inside of.
    start = 0
    end = n-1
    
    # We are going to search for alphabets in our array that come after the given alphabet
    # in alphabetical order. 
    
    # And we need to return the alphabet thats least furthest from the given alphabet.  
    res = -1
    
    # Im going to run a binary search and im going to be searching for alphabets that come after
    # the given alphabet in order.
    
    # alphabet = 'b' => 'c' > 'b' => True, 'd' > 'b' => True, 'b' > 'a' => True, 'b' > 'z' => False
    
    # So whenever i find an alphabet that comes after the given alphabet in alphabetical order then i store
    # its index in the variable and continue my search in its left portion since i want to find the alphabet
    # thats least further away from the given alphabet and if i go to the left side i have a chance of finding
    # an alphabet which is even more closer to the given alphabet then the current ive found.
    
    while start <= end:
        
        mid = (start+end) // 2
        
        # In case if my mid pointer is pointing at an alphabet which comes after the given alphabet in order
        # then that means this is a possible candidate for being the least furthest as well so i store its 
        # index in our answer.
        if arr[mid] > alphabet:
            res = mid
            # But after finding it i continue my search on its left portion cause i could still find an 
            # alphabet that could be even more closer than this alphabet.
            end = mid-1
        else:
            # In other cases where the pointed alphabet is less than the given alphabet then that means 
            # this alphabet comes before our given alphabet in those cases i wanna shift my search to the
            # right side cause thats where alphabets that come after the given alphabet could lie inside of.
            start = mid+1
            
    return res

print(nextAlphabet(['a','b','c','d','f','i','z'],7,'x'))