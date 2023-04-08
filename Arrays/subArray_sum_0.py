# Good But NOt Good

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        
        for i in range(n):
            subArraySum = 0
            for j in range(i,n):
                subArraySum+=arr[j]
                if subArraySum == 0:
                    return True
        
        return False

# Optimal 

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        
        currSum = 0
        prefixSums = set()
        
        for i in range(n):
            currSum+=arr[i]
            if currSum == 0 or currSum in prefixSums:
                return True
            else:
                prefixSums.add(currSum)
        
        return False