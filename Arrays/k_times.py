# Space Compexity: O(n)
# Time Complexity: O(n)

class Solution:
    
    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        counter = dict()
        ans=0
        
        # Counting the frequency of each element in the array using the hashmap
        for num in arr:
            if num not in counter:
                counter[num] = 0
            counter[num]+=1
        
        # Iterating through each key value pair in the hashmap
        for key,val in counter.items():
            
            # The elements who have their frequency greater than n/k 
            # we increment our answer cause we have found an element that
            # exists more than n/k times in the array.
            if val > (n/k):
                ans+=1
        
        # We return the number of elements that we have found to exist greater 
        # n/k times in the array.
        return ans