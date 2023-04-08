# Better than O(n^2)

# Space Complexity: O(n)
# Time Complexity: O(n)

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq = dict()
        n = len(nums)

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num]+=1
        
        return [key for key,val in freq.items() if val > (n/3)] 

# Optimal Using Boyer Moore's Voting Algorithm

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        # A variable to store our 1st majority element and also a variable to store its counter 
        # as to how many more majority 1 elements we have over our minority elemets
        majority1=count1=0

        # Similarly we will have a variable to store or 2nd majority element that might or might 
        # not exist but we have to check and similarly we will have a counter as well
        majority2=count2=0

        # Iterating through the array and finding our 1st and 2nd majority elements we will do it
        # by finding all instances of our majority elements and decrementing them by our minority
        # elements in the end since majority elements are always more than the minority we should
        # have both of our majority elements in their respective places.

        for num in nums:
            
            # If the element we are iterating through is equal to our majority1 element then we have
            # found another instance of our majority1 element in the subarray hence we increment count1
            # suggesting the amount majority1 elements have increased even more than the minority elements.
            if majority1 == num:
                count1+=1

            # Similarly if the element we are iterating through currently is equal to our majority2 element
            # then we increment count2 cause we have found another instance of the element in our 
            # subarray hence we increment coutn2 suggesting our majority2 elements have increased by one
            # more than our minority elements.
            elif majority2 == num:
                count2+=1
            
            # Count1 will be zero in two cases Once during the first run and more times whenever
            # the number of majority1 elements is equal to our minority elements during the first
            # run we will just our majority element to whatever element we are currently on right now
            # But in the second case we intialise with our current element and reset the counter
            # and initialise a new subArray from scratch for our majority1 element hence we reset counter
            # as well.  
            elif count1 == 0:
                majority1=num
                count1=1
            
            # Similar to first case we do the same thing again and initially when count2 is zero that means
            # we havent set a majority2 element so we set it in this case to the number we are on right now.
            # Second case this triggers is when the number of minority elements and number of majority elements
            # are equal to each other in the current subArray that we have built hence this means we have selected
            # the wrong element as our majority element hence we have to change to a new element and we also 
            # initiate a subarray in our array for this element and set counter to 1.
            elif count2 == 0:
                majority2=num
                count2=1

            # Else case we have discovered a minority element hence we are going to decrement both the 
            # counts since a new minority decreases the difference between the majority and minority
            else:
                count1-=1
                count2-=1

            # After the iteration of the loop we will have both the majority elements i stored in there respective variables.
            
        # Next Thing we need to check if these majority elements meet the given conditions by checking if both the elements
        # exist more than n/3 number of times in the array or not cause it is not confirmed if they do or not. 
        freq1=0
        freq2=0

        for num in nums:
            if num == majority1:
                freq1+=1
            elif num == majority2:
                freq2+=1

        ans = []

        if freq1 > (n/3):
            ans.append(majority1)
        
        if freq2 > (n/3):
            ans.append(majority2)
        
        return ans