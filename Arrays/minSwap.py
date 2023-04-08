import math
def minSwap (arr, n, k) :         
        swaps = math.inf
        
        # Counting the numbers which are less than or equal to k.
        good = 0
        
        # Counting all the numbers which are less than or equal to k and thats
        # going to tell us how many numbers do we have to bring together into one
        # contigeous subarray.
        for num in arr:
            if num <= k:
                good+=1
        
        if good == 0:
            return 0
        
        # Now i need to check each contigeous subarray of size which is equal to
        # the numbers we have which are less than or equal to k in our array.
        
        # Why should i check each contigeous subarray of such size? 
        # Cause thats the size of the subarray we have to form in our array in 
        # which all the elements are less than k.
        
        # And the way im going to do that is by modifying an existing subarray
        # of the same size
        
        # So im going to check which subarray i can convert into a subarray which
        # has all elements less than k with minimum number of swaps
        
        # So for that im going to check each subarray of such size.
        
        # And how will i check how many swaps does it require that is through
        # checking how many numbers it has which are greater than k becuase
        # i would need to swap them in order convert the contigeuos subarray
        # into a subarray full of elements less than k.
        
        # So the subarray which consist of minimum numbers which are greater than 
        # k would require the least amount of swaps hence that would be the minimum
        # swaps we are required to do in order to bring all the elements less than
        # k equal
        
        i = 0
        j = good-1
        bad = 0
        
        # Calculating all numbers greater than k in our first subarray
        for x in range(i,j+1):
            if arr[x] > k:
                bad+=1
        
        while j < n:
            # Checking for each subarray if it has the least amount of swaps or not.
            swaps = min(swaps,bad)
            
            # Shifting the pointers to check for a different subarray 
            
            # If the current ith pointer was pointing at a element which was
            # greater than k then i decrement bad cause this element isnt going
            # to be in our new contingous subarray that we are going to create.
            
            if arr[i] > k:
                bad-=1
            i+=1
            
            # If the new element that my j pointer is going to point to in the 
            # new contingnous subarray is greater than k then i increment bad
            # as a new number greater than k is inside of it
            
            j+=1
            if j < n and arr[j] > k:
                bad+=1
            
        return swaps
    
print(minSwap([10, 12, 20, 20, 5, 19, 19, 12, 1, 20, 1],11,1))