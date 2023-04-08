def findLangford(n):
    # Array to store my valid langford sequence
    ans=[]
    
    # Creating a function to generate a valid langford sequence for us.
    def langfordSequence(n):
        
        # If n is equal to 0 that means we have generated a valid sequence
        # and we return True.
        if n == 0:
            return True
        
        # Iterating through all valid indexes where I can place n and I can also
        # place its next instance in correspondance where I placed its first instance.
        for i in range(len(ans)-n-1):
            
            # Checking to see if the both the places where i would need to place n 
            # in order to generate a valid pairing is empty
            if ans[i] == 0 and ans[i+n+1] == 0:
                
                # If they are empty then I insert n into those spots
                ans[i] = n
                ans[i+n+1] = n
                
                # Then i need to check if by placing n at this spot its still allowing
                # other values in the range to take there spot
                
                # So i need to call a recursive function that would fill the next 
                # value for me here
                
                # If that value can successfully find a valid spot for itself
                # then it would return True
                if langfordSequence(n-1):
                    # So we also return True since the spot we chose has helped to
                    # generate a valid langford pairing
                    return True
                
                # If we got False that means this spot that we chose to add 
                # our n value at didnt allow other values in the range to 
                # take there own valid places so we undo our changes since 
                # we werent able to generate a valid langford pairing by
                # placing n at that index so we undo changes and check if 
                # we can generate a valid pairing by placing n at other 
                # valid indexes of n.
                ans[i] = 0
                ans[i+n+1] = 0
             
        # We return false if none of the valid indexes for n were empty
        # so others values can be notified and they undo there changes
        # and test there other valid indexes.
        return False
       
    
    # If N isnt a valid value for which we can generate a valid langford           
    # sequence for then we return [-1]
    if (n % 4 == 1 or n % 4 == 2):
        return [-1]
    langfordSequence(n)
    return ans    