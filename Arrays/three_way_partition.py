def threeWayPartition(self, array, a, b):
	    
	    # A pointer which is going to traverse through the array.
        k = 0
	    
	    # A pointer to partition all the elements less than a to the right side
        i = 0
        
	    # A pointer to partition to all the elements greater than b to the left
	    # side	    
        j = len(array) - 1
	    
	    # Utility Swapping Elements Function:
        def swap(x,y):
            temp = array[x]
            array[x] = array[y]
            array[y] = temp

        # Running the loop until the traversing pointer goes pass the jth pointer
	    # cause then its going to start traversing through elements that i have
	    # partioned on to the left side and starting swapping them and we dont want
	    # that to happen
        while k <= j:
	        # First case im traversing through an element which is less than a
	        # then in that case I need to bring onto the right side by swapping
	        # it with the value on the current ith index
	        
	        if array[k] < a:
	            # If its less than the a then i swap it with the current ith index
	            # value 
	            swap(i,k)
	            # Since the element ive swapped is from the left side and ive 
	            # already traversed through that side and checked all the elements
	            # then i dont need to check them again so i increment my pointer k
                k+=1
	            
	            # Since the current ith index is filled with a valid value less than
	            # a hence i increment it to a new index
                i+=1
	       
	        # Second case im traversing through an element which is greater than b 
	        # hence i need to bring it on my left side for that ill be swapping it
	        # with the current jth index value.
            elif array[k] > b:
                swap(j,k)
	            
	            # Since the current jth index is filled with a valid value less than
	            # a hence j increment it to a new index
                j-=1
	            
	            # This time i will not increment k cause i need to make a check 
	            # on that value that i have swapped over from the right side cause
	            # i cause havent traversed through that side before so i need to 
	            # apply a check on the value that ive swapped over from that side.
	            
            else:
	            # If that element meets none of the cases then im going to ignore
	            # cause its an element between a and b or its a and b themeselves
	            # and by partioning the right and left side these elements are 
	            # automatocally going to be brought to the middle so i ignore them
                k+=1
        return array