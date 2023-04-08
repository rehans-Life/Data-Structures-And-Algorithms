def mergeIntervals(intervals):

    # An Array to store all my non overlapping intervals
    ans = []

    # This is going to store the merged intervals
    pair = intervals[0]

    # Iterating through all the intervals
    for interval in intervals:
        
        # If our current interval in iteration merges with the current merged interval
        # that we have then we add it to our current merged interval.
        if interval[0] <= pair[1]:
            pair[1] = max(pair[1],interval[1])
        else:
            # Else it means that our current merged interval is a non overlapping
            # interval since the intervals are sorted hence we append it to our 
            # answer
            ans.append(pair)
            # Then we check our current interval which didnt overlap with any our
            # current merged interval and see if it overlaps with any other pairs.
            pair = interval
    
    ans.append(pair)

    return ans