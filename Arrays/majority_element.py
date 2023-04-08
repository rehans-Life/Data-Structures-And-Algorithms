# Boyer Moore's Voting Algorithm

# Space Complexity: O(1)
# Time Complexity: O(n)

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Counter to count how many more of the majority elements exists over the minority
        count=0

        # Variable which is going to store the value of the element that we have considered 
        # to be our majority element
        majority=0

        # Iterating through all the elements and we can keep going to cancel our the minority from
        # our majority and in the end we will have our majority element in our variable why because 
        # majority is always more than the minority so its never going ot be able to cancel our the 
        # majority elements
        for num in nums:
            
            # If the count is zero then either this is the start of the iteration or we have reached
            # a point where there are no majority elements left in a particular section of the array
            # hence we start from scratch by considering the next element as our majority element. 
            if count == 0:
                majority = num
            
            # If we run into a number a thats equal our to majority element then we increment the counter
            # majority is now one more than the minority
            if majority == num:
                count+=1
            else:
                # If we see a minority we decrement the majority element cause we have one minority so
                # number of minority is increased and the edge the majority has over the minority has 
                # decreased as well.
                count-=1

        return majority