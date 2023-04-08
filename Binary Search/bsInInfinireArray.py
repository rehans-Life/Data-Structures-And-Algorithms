def bs(arr,start,end,num):

    while start <= end:
        
        mid = (start+end) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    
    return -1

def searchInfiniteArray(arr,n,num):
    
    # Initialize two pointers which are going to denote the range in my array within which
    # my element of interest lies inside of.
    start = 0
    end = 1

    # Im going to keep on changing the range as long as the element which im trying to find
    # is between our range
    
    # Im going to check if its within the range or not by checking if the last value of the 
    # range is greater than the given value if not then im going to keep on creating ranges
    # in forward direction until i create one which consist of the given element.
       
    while num > arr[end]:
        start = end
        end*=2
    
    # Implementing binary search on the range which consist of the element of interest so i can
    # find it in the array.
    return bs(arr,start,end,num)

arr = [6,9,11,15,16,18,21,25]
# for i in range(1,1000):
    # arr.append(i)

print(searchInfiniteArray(arr,len(arr),16))