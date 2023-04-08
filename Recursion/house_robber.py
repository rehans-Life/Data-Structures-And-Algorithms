def house_robber(arr):
    def helper(arr,i=0,sumation=0):

    # If we have finished robbing the houses on the street we return the amount we have robbed.
        if i >= len(arr):
            return sumation
    

    # One option is to rob the house that im currently on and if i do that i cant rob the house
    # next to it thats im incrementing pointer i by 2.
        option1 = helper(arr,i+2,sumation+arr[i])

    # Another option is to not rob the house that im currently on and if i do that then i can
    # rob the house next to it.
        option2 = helper(arr,i+1,sumation)

    # Returning the greater of the two sums that im able to rob.
        return max(option1,option2)

    return helper(arr)

print(house_robber([2,7,9,3,1]))