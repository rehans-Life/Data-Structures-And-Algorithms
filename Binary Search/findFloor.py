class Solution:
    def findFloor(self,A,N,X):
        #Your code here
        
        # Setting up two pointers denoting the start and end range of our search
        start = 0
        end = N-1
        
        res = -1
        
        while start <= end:
            
            mid = (start+end) // 2
        
            # If my mid pointer is currently pointing at element which is equal 
            # to our give element then i return that index itself.
            if A[mid] == X:
                return mid
            
            # If my mid pointer is currently pointing at elements which is greater
            # than given element then that means the elements less than X lie in 
            # left side of the array so i shift my range to that index.
            if A[mid] > X:
                end = mid-1
                
            # If my mid pointer is currently pointing at an element which is less
            # than given element then this could be our possible answer hence we 
            # need to store it in our result but continue our search on the right side
            # to find elements which are greater this elements but less than X 
            # cause we need to return the greatest element less than X. so we keep
            # searching for grrater elements.
            else:
                res = mid
                start = mid+1
        
        return res