def longestUniqueSubStr(s: str):
    
    # Maintaining two pointers for the start and the end of the
    # window.
    i,j=0,0
    
    # A hashmap to store the unique elements of a window along with
    # there frequencies
    unique = dict()
    
    n = len(s)
    
    maxSubString = 0
    
    while j < n:
        # I keep adding the elements that my j pointer is traversing
        # through into my hashmap
        if s[j] not in unique:
            # If the element is not in the hashmap then i add it
            # since its a new unique element now.
            unique[s[j]] = 1
        else:
            # If its already there then that means i have found 
            # another instance of that element.
            unique[s[j]]+=1
            
        # If the number of unique elements inside of the substring is
        # equal to the number of elements in it then that means all 
        # elements are unique in that substring.
        if len(unique) == (j-i+1):
            
            # I need to check if the length of the given subString
            # is greater than the current maximum substring that ive
            # found.
            maxSubString = max(maxSubString,(j-i+1))
        
            # Im incrementing to then look at the next substring of
            # starting from the same element because thats going to be
            # of greater length and has the potential to beat my current
            # longest unique substring.
            j+=1
        
        # Case II is when the number of unique elements is less than
        # the length of the substring then that means there are some
        # repeating elements in the substring
        
        # In that case i move to the next element cause that has the
        # cause I know this element will not generate a substring of non 
        # repeating now of greater length then my current answer.
        
        elif len(unique) < (j-i+1):
            
            # Before moving to the next element i have to remove its
            # count from the hashmap cause its not going to be in my 
            # new substring. anymore.
            unique[s[i]]-=1
            
            # If that was the only occurence of that element in the substring
            # then this element should be completely deleted from the hashmap
            # because there are no instances of it left in the substring
            if unique[s[i]] == 0:
                del unique[s[i]]
            
            i+=1
            j+=1
    
    return maxSubString
            
print(longestUniqueSubStr('dbdedbfghdbd'))           
            
                