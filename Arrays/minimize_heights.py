def getMinDiff(self, arr, n, k):
        arr.sort()

        # Creating two variables min and max to store the minimum and maximum values in a certain 
        # alternative
        minimum = maximum = 0

        # Creating a result named variable which is going to store our minimum 
        # difference between our longest and shortest tower

        # Its initialized with the difference b/w our longest and shortest 
        # tower in unmodified array
        minDiff = arr[n-1] - arr[0]

        # A loop to iterate through each element so we can test out each
        # consecutive pair

        # We will increment the smaller value in the consecutive pair and 
        # decrement the larger value so that we can minimize the difference
        # between them even more 

        # And since this is a sorted array the consecutive numbers already
        # have a small difference but if we minimize the difference even more
        # the difference will decrease even more

        # The way we maximize is by incrementing the smaller value by k 
        # and minimize is by decrementing the larger value by k

        # But still the only way we can consider there difference as valid
        # asnwer only if the the smaller value by incrementing becomes the largest
        # tower in the array and if the larger value by decrementing becomes
        # the smallest value in the array.

        # Cause then these two numbers would form the smallest and the longest 
        # towers.

        # We are starting from index 1 is because our first tower cannot be minimized
        # cause that would only lead to increasing the distance.

        # Same goes for our longest tower as well.

        for i in range(1,n):

            # We will always form the consecutive pair from the ith elment ard the 
            # element behind it and since the ith element then would be the larger
            # number of the two then we need to minimize it to minimize the diff
            # of the consecutive pair

            # But if ith element is less than k then we cant decrement it cause
            # it would become negative and we are not allowed to take negative
            # values here

            if i >= k:

                # Checking if the minimized ith value is the smallest value
                # in the array we can check it by comparing it with the 
                # incremented value of the smallest tower.
                minimum = min(arr[i]-k,arr[0]+k)

                # Then we check if the incremented smaller number is in the 
                # largest number in the array we check by checking it with
                # decremented longest tower height cause in the resulted
                # it will always be decremented in order to let us find the minimum
                # value.
                maximum = max(arr[i-1]+k,arr[n-1]-k)

                # We check the consecutive pairs difference and see if its less than
                # the previous one if it is then its set as the new minimized
                # difference b/w the longest and the shortest tower.
                minDiff = min(minDiff,maximum-minimum)
            
            else:
                continue

        return minDiff