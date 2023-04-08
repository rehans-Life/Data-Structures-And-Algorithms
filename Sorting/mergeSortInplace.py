def twoWayMerge(arr,start,mid,end):
    # Index pointer for the start of our right sorted section.
    start2 = mid+1
    
    # Running a while until either of the index pointers go pass the length of there respective sections.
    while start <= mid and start2 <= end:
        
        # If the right sorted section value is less than the left sorted section value then that means
        # its already in the right position so we just move the index pointer to the next element.
        if arr[start] < arr[start2]:
            start+=1
        else:
            # When the left section's index pointer value is smaller in that case you have to 
            # shift all the elements behind start2 pointer till the start pointer by one index to
            # the right 
            
            # In that way you will create space for your start2 element in the start position which 
            # is where it should be placed at.
            
            # Before the shift the values you store the value of your start2 index
            value = arr[start2]
            
            # Pointer which is going to move as we shift the elements by one position to the right
            i = start2 
            
            # We want shift all the elements which come before the start2 index till start index 
            # so till this pointer reaches start pointer we keep shifting 
            
            while i != start:
                arr[i] = arr[i-1]
                i-=1

            # After shifting all the values we have created space at the start index to place
            # the correct value
            arr[start] = value
            
            # Then we know that the start index value got shifted to the right so we have to accordingly
            # move our start pointer to that element
            start+=1
            
            # Same for our ending value of our left section it got shifted by one element so we shift 
            # our mid pointer as well
            mid+=1
            
            # Then since we have sorted the current start2 index value then we move to the next value 
            # in our right side
            start2+=1
    

def mergeSortInPlace(arr,start,end):
    if start < end:
        mid = (start + end) // 2
        mergeSortInPlace(arr,start,mid)
        mergeSortInPlace(arr,mid+1,end)
        twoWayMerge(arr,start,mid,end)

arr = [15,2,-5,4,-10,6,8,-1,12]
mergeSortInPlace(arr,0,len(arr)-1)
print(arr)