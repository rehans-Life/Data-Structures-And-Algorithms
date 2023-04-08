class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # Converting the array into a set cause its more efficient to search in it
        numsSet = set(nums)

        # Varaible to store the length of our longest cosecutive Sequence
        longest = 0

        # Running an iteration through each Number and finding the numbers we can initiate
        # consecutive sequence from

        for num in nums:

            # Checking to see if the number has its left consecutive number in the array
            # or not cause if it does then we cannot start our consecutive sequence from
            # this number or if it doesnt then we initiate our sequence.
            
            if (num-1) not in numsSet:
                    
                    # Length variable to store the length of the sequence that we are generating
                    length = 0

                    # As the length increases we are going to keep searching for the next consutive number
                    # in the array until we dont find one.
                    while (num + length) in numsSet:
                        length+=1

                    # Checking to see if our current sequence length is a candidate for our longest sequence
                    # length
                    longest = max(longest,length)

                    # This iteration ends here and move on to checking if we can create a consective sequence
                    # out of the next number

        # We return the length of the longest subsequence that we have generated up until now.
        return longest