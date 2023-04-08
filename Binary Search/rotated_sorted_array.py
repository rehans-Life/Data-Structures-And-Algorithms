def rotations(arr,n):
        # You have been given a rotated sorted array
        # and you need to find the number of times
        # it has been rotated.
        
        # For this if you are able to find the minimum 
        # elements index then you will be able denote
        # that as the number of rotations you array
        # has been through.
        
        # Setting up the range of search through the two
        # pointers
        
        start = 0
        end = n - 1
        
        # Covering the edge when zero rotations have been made hence
        # in that the first element is going to be my smallest number
        left = (start+n-1) % n
            
        right = (start+1) % n
            
        if arr[left] > arr[start] and arr[right] > arr[start]:
            return start
        
        while start <= end:
            
            mid = (start+end) // 2
            
            # Now i need to check if the current mid pointer is at 
            # the minimum most value or not and for that i need to
            # check if its less than both of its neighbours or not
            left = (mid+n-1) % n
            
            right = (mid+1) % n
            
            if arr[left] >= arr[mid] and arr[right] >= arr[mid]:
                return mid
            
            # Now the second case is when im not pointing at minimum
            # most value in that case i need to identify which sorted
            # section of the array im in 
            
            if arr[end] <= arr[mid]:
                # If my mid pointer is greater than the end value then
                # im in left sorted array and in that case i need to move
                # to the right side becuase my minimum element lies in the
                # right sorted section of the array.
                start = mid+1
                
            else:
                # if my mid pointer is less than the end value then im
                # already inside of my right sorted section hence that means 
                # that i need to move to the left of the right sorted 
                # section to find its minimum element.
                end = mid - 1