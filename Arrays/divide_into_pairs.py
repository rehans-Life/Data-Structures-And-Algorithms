# Brute Force

# Space Complexity: O(1)
# Time Complexity: O(nlog(n)+n) => O(nlog(n))

class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        # Sorting the array so that equal elements are placed next to each other
        nums.sort()

        n = len(nums)
        # Number of Pairs we need to divide our array into.
        pairs = n / 2

        # Pointer initially pointing at element with index 0
        i = 0

        # Iterating until our pointer reaches the end of the array
        while i < n:

            # If two consecutive elements arent equal then that means we wont be able to form n number
            # of pairs such that elements inside of each pair are equal.

            # Cause we wont be able to create a pair with element at index i where elements are equal
            # since there is no other element with the same value it has 

            # I know that since in a sorted array elements with equal value are placed next to each
            # other so if the element next to the ith element isnt equal in value then there is no
            # other element with the same value as the ith element.

            if nums[i] != nums[i+1]:
                break 

            # If the consecutive elements are equal then that means i have found a valid pair hence 
            # i decrement that pairs value cause i have formed a value a pair

            # Im incrementing i by 2 steps cause we have used the ith element and the element next to
            # it in a pair so i need to skip the next element as well.
            else:
                pairs-=1
                i+=2
        
        # If our pairs counter has reached 0 by the end of the loop we return True cause we have divided
        # the array into n number of pairs or else we return False and that would be the case where the 
        # element next to the ith element wasnt equal in value and that suggested we wont be able to
        # form a pair with the ith element where the element next to it in the pair is equal to it
        # cause if the element next to it inst equal it then there is no other element in the array
        # equal to it as well.
        return True if not pairs else False   

# Optimal Approach

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        # We maintain a hashmap to store the frequency of each element in the array.
        freq = dict()

        # Counting the frequency of each Number
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
        
        # Checking the if the frequencies of each element is even, if not we return false
        # cause that means we wont be able to divide the array into pairs of n where the 
        # given conditions meet
        for num in nums:
            # If the frequency is not odd for any of the numbers in the array
            # we return false.
            if freq[num] % 2 != 0:
                return False
        
        return True

# Optimal 2 - One Loop:

class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        # A hashset which is going to check which elements
        # we have iterated through already
        seen = set()

        # A counter as to how many valid pairs we have found
        # in the array.
        total = 0

        for el in nums:

            if el in seen:
                # If we have seen it then we have formed a valid
                # pair so we increment totol
                total+=1

                # We remove the element from the set that we 
                # added previously so we can form more pairs
                # with the same element as well if there exists
                # more of the same elements
                seen.remove(el)

            else:
                # If we havent seen the element before we add
                # it to the set to see if we can form a pair
                # with it or not.
                seen.add(el)
        
        return total == len(nums) / 2