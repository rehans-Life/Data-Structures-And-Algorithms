# Optimal Approach:

# Time Complexity: O(m+n)
# Space Complexity: O(1)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        # l pointer which is going to pointing at the end of our nums1 array
        l = m+n-1

        # Pointer i pointing at the end of the nums2
        i = m - 1

        # Pointer j pointing at the end of the nums2
        j = n - 1

        # Filling the nums1 array as our merged sorted array in reverse order
        while i >= 0 and j >= 0:
            
            # If the ith element in my nums1 array is greater than the jth element in my
            # nums2 array we place the ith element in the lth index
            if nums1[i] > nums2[j]:
                nums1[l] = nums1[i]
                # Incrementing our ith pointer to point to the next largest element in the 
                # array 
                i-=1
            # If the jth element in my nums2 array is greater than the ith element in my nums2
            # array we place the jth element in the lth index of my sorted array
            else:
                nums1[l] = nums2[j]
                # Incrementing our jth pointer to point to the next largest element in the 
                # array 
                j-=1

            # Either way whichever arrays index takes the current lth index we want to move it 
            # backwards cause the current lth index has been filled by an element.  
            l-=1
        
        # Edge Case: When ive finished traversing through all the elements in my nums1 array
        # but there are still some elements remaning in my nums2 array that are yet to be added 
        # to my nums1 array to form the complete merge sorted array.

        # Then i run another iteration through my nums2 array and fill the elements starting 
        # from my current lth index

        while j >= 0:

            # Adding the jth element to my lth index in my nums1 array.
            nums1[l] = nums2[j]

            # Decrementing j to point towards the next remaning elements
            j-=1

            # Decrementing the l pointer to point to a new index so the next element can inserted
            # into another index
            l-=1

nums1 = [1,4,6]
nums2 = [2,5,7]

solution = Solution()