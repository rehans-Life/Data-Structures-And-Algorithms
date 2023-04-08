# Brute Force.

# Space Complexity: O(n)
# Time Complexity: O(n^2)

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]: 
        
        results = [True] * len(candies) 

        for i in range(len(candies)):
            newAmountOfCandies = candies[i] + extraCandies
            for j in range(len(candies)):
                if candies[j] > newAmountOfCandies:
                        results[i] = False
                        break
                        
        return results


# Optimal

# Space Complexitt: O(1)
# Time Complexity: O(n)

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int): 
        
        # Finding the greatest Number of Candies a Kid has.
        greatest: int = max(candies)

        # Iterating through each kid giving them my extra candies and then checking if
        # they have the greatest number of candies or not

        # If they do then im setting their index value to True or else im setting it to
        # False

        for i,kidCandies in enumerate(candies):
            candies[i] = (kidCandies+extraCandies) >= greatest
        
        # Then im returning the array of True and False values.
        return candies