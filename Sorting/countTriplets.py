def countTriplets(arr,n,target):
    
    arr.sort()
    count = 0
    
    # We need to iterate through all possible elements in the arrys that can form triplets of three
    # and we know last two elements wont be able to form triplets of three so we will never check them
    
    for i in range(n-2):
        
        # j will initially be placed at j+1 cause thats the first number my ith element can form a
        # pair with
         
        j = i+1
        
        # k will be placed at the end of the array so i can instantly find all possible triplets that
        # can give us sum less than given sum for a paritcular jth element
        
        k = n-1
        
        # When j and k become equal then in that case ive checked all possible triplets that could've given
        # us sum less than given sum for the current ith element.
        
        while j < k:
            
            # When sumation of i,j and k is greater than or equal to given sum then that means that i and j 
            # when combined with the kth element will not give us a sum less than the given sum hence that
            # means if i take pair of ith element with other elements infront of j then they wont give us a lesser 
            # sum why because they are only going to be greater than current jth element therefore increase
            # the sum even more
            
            # So i decrement k so that i dont have to check other jth elements triplet with this number again
            
            if arr[i]+arr[j]+arr[k] >= target:
                k-=1
            
            # When sumation is equal then i can find all possible triplets of i with the current jth element in one
            # go 
            
            # Cause since the current kth element is giving us a sum less than given sum then all elements that come before
            # our current kth element and after our jth element will also give us a triplet sum of less than given sum
            # cause they are only going to be less than current kth element
            
            # So increment count by not only by 1 but by the number of elements that come after j until k cause they all
            # will give us a triplet sum of less than given sum
            
            else:                
                count+=(j-k)
                
                # Now since ive found all possible triplets formed with pairing of i with our current jth element then i will
                # increment j so that i can check for possible triplets of i with the next element as well
                j+1
        
        return count
            
    