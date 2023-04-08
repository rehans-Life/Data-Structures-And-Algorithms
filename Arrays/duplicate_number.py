class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        # Starting a fast and a slow pointer from the starting node of our represented linked list which 
        # is the node labelled with index zero cause no other position is ever going to point at it since 
        # none of the positions are going to have an element with value 0 since the range of elements is from
        # 1 to n always
        slow = fast = 0

        # Starting from traversing until we find the colliding point

        # We move the fast pointer by two nodes while slow pointer by one node.

        while True:

            # The Elements value represent the next node we need to traverse to.
            fast = nums[fast]
            fast = nums[fast]

            # Then moving the slow pointer by node at a time
            slow = nums[slow]

            if slow == fast:
                break

        i = 0

        # Starting a traversel from the start of the linked list one by one and also starting a traversal
        # from the colliding point of the slow and fast nodes.

        # When they intersect we stop our traversel cause then we have found our starting point of the 
        # cycle

        while i != slow:

            i = nums[i]
            slow = nums[slow]

        # We return the starting point of the cycle cause that index represents 
        # the duplicate value.
        return i