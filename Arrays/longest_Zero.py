# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        # We need a variable to store the length of the longest subarray with sum 
        # zero
        maxi = 0
        
        # We need a variable to store the prefixSum till a certain index
        # We increment this upon each iteration.
        currSum = 0
        
        # This is going to store the prefix sum at each index.
        prefixSums = dict()
        
        # Iterating through the array to find subArrays with sum zero
        
        for i in range(n):
            # Incrementing the current sum by the ith element to get the new 
            # prefix sum
            currSum += arr[i]
            
            # Then we need to check two things
            # 1) if prefix Sum is zero then that means that starting from the 
            # 0th index till our ith element the subArray forms a sum of zero 
            # hence we can make that length compete for being the maximum subArray
            # with sum zero actually dont even make it compete cause 100% till this
            # beat any subArray length of sum zero that we have found till now.
            
            if currSum == 0:
                maxi =  i + 1
            
            # 2) If prefix Sum has already been generated at a another point in the
            # array hence that means elements between that index where we previosly
            # got this sum till our current index form a sum of zero cause only 
            # then we were able to get the same prefix Sum hence we have discovered
            # a subArray with sum zero.
            else: 
                if currSum in prefixSums:
                    # We will make this subArrays length compete against our current 
                    # max  length subarray with sum Zero cause we need to return 
                    # length of subArray which gives a sum of zero and also has the 
                    # maximum length
                    maxi = max(maxi,(i-prefixSums[currSum]))
                    
                # If this prefix isnt in our prefixSums then we add it as a key value
                # pair where sum if the key and the index hwere we got this sum is
                # the value to that key
                else:
                    prefixSums[currSum] = i
            
        return maxi    


