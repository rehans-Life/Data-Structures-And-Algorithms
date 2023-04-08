def house_robberII(arr):
    def helper(arr,i=0,sumation=0,robHouseI=False):

        if i >= len(arr):
            return sumation
                    
        if robHouseI and i == len(arr) - 1:
            return sumation

        # If im on the first house and i choose to rob it then im going to set robHouseI to true
        if i == 0 : 
            robHouseI = True
        
        option1 = helper(arr,i+2,sumation+arr[i],robHouseI)

        # If im on my first house and i dont choose to rob it then im going to set robHouseII to
        # false
        if i == 0:
            robHouseI = False

        option2 = helper(arr,i+1,sumation,robHouseI)

        return max(option1,option2)
    return helper(arr)
print(house_robberII([1,2,3]))