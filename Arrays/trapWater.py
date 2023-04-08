class Solution:
    def trap(self, height: list[int]) -> int:

        # Note: In order to calculate how much water a particular bar can contain we need the heights of the max bars on both the left and right 
        # sides of the bar we want to find how many water it can store

        # Then we use the minimum of both the max bars to determine how much water can be stored in that block

        # WHY MINIMUM?

        # Becuase the height of minimum bar will tell us upto how many units we can fill the water in this block before we start spilling it
        # Also another thing thats going to determine the units of water we can fill inside is the height of the block/bar itself becuase
        # the height is going take up the units of water can fill.

        # A left pointer which is going to traverse through our array from the left and keep track of our leftMax value
        l = 0
        leftMax = height[l]

        # Similarly a right pointer to traverse from the right of our array and keep track of the rightMax value we have discovered up until now.
        r = len(height) - 1
        rightMax = height[r]

        ans = 0

        # We are going to iterating until they meet because when they do then that means we have checked all the bars.
        while l < r:
            
            # If leftMax is less than the rightmax then we shift our left pointer cause then that means that we will be sure that the left
            # max is going to be our new left bars minimum
            if leftMax < rightMax:
                # Incrementing the left point to a new left bar
                l+=1
                # From our new bar we sure that its left sides maximum is less than the right sides maximum hence in order to caculate the 
                # water that can be stored in our current left bar we just need to find the diff b/w our curr bar and leftMax up until now
                unitsOfWater = leftMax - height[l]

                # If the current left bar can store water diff would be greater than zero and we increment our answer by that value
                if unitsOfWater > 0:
                    ans+=unitsOfWater

                # Then we check if our current l pointer value is the max we have discovered from that start.
                leftMax = max(leftMax,height[l])            
            
            # If rightMax is less than the leftMax then that means if we increment our right pointer to a new bar cause we will 100%
            # be sure that the its rightMax value is the minimum of the two max's hence we can easily calculate our new bars value.
            else:
                # Decrementing the right pointer to a new right bar cause we will be sure that we can easily calculate the water
                # it can hold cause we the minimum of its max bars of both sides.
                r-=1

                # We know for sure the minimum max for this new right bar is our current right max value. 
                unitsOfWater = rightMax - height[r]

                # Then we check if the current right bar is actually able to store water or not if it can then we increment our answer by the units
                # it can store
                if unitsOfWater > 0:
                    ans+=unitsOfWater
                
                # Then we check if this new element discovered on the right side is less than the current right max we have cause then this element is going
                # to become the max of the right side
                rightMax = max(rightMax,height[r])
            
        return ans