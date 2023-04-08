import math

class HashSet:

    def __init__(self):
        # Containg an array of size which is equal to all the possible values that can be added to a set.
        self.mark = [0] * math.floor(1e6)

    def add(self, key):

        # Whenever someone tries to add a value to a set then i mark the index which is equal to that value as 1 denoting that it has
        # been added.
        self.mark[key] = 1

    def remove(self, key):
        
        # If the index equal to the value they want to remove is marked as one then that means that the value is there in my set.
        if self.mark[key] == 1:

            # Now i mark the index which is equal to the value they want to remove as 1.
            self.mark[key] = 0

            # Then I return the value i just removed.
            return key
        else:
            # If the index equal to that value wasnt already marked as 1 then i return -1.
            return -1

    def contains(self, key):

        # Returns True if the index equal to that value is marked as one or else returns False.
        return True if self.mark[key] == 1 else False