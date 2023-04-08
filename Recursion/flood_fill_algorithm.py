# Lets say we have this image represented as a 2d Array. 

# And we are given a certain coordinate on the 2d Array.

# Now we need to change coordinates number to the given
# number 

# We also need to look at the adjacent nodes to the given
# node and if there values are the same as the given 
# coordinates value you need to change there values to
# new Values

# Then you would have also to traverse to these adjacent 
# nodes whose values you just changed and look at there
# adjacent nodes and see if any of there values match 
# your given node and you keep repeating this process
# until you dont have any adjacent nodes whose values
# can be changed

image=[
    [1,2,7,5],
    [1,3,3,3],
    [6,5,5,3],
    [2,2,3,3]
    ]

coordinate=(1,2)

newColor = 8

# So the given coordinates value is 3.

# We need to not only change its value to three but also change
# its adjacent corodinates values to given value as well whose
# whose previous values were the same as the given coordinates 
# value.

# Then you repeat the same process again for the adjacent 
# coordinates as well. You look at there adjacent coordinates
# and see if any of there values are the same given coordinates
# value and change there values as well.

# You keep repeating until there are no adjacent nodes with the 
# same value as the given cooridinates value.


# So in your function your given the image which is a 2d Array
# and your given coordinates x and y and these are the coordinates
# whose value you need to change to the newColor

def flood_fill_algorithm(image,x,y,newColor):

    # Storing the given coordinates value in a variable 
    # so in future we can compare other adjacent coordinates
    # value with the given coordinates value.
    oldColor = image[x][y]

    # Storing the last rows index in a variable it will help
    # us in checking if we are trying to access a coordinate
    # which is out of the boundry of the image or not.
    n = len(image) 

    # Doing the same thing for the column storing the last column 
    # in a variable so in future we can check if we are trying to
    # access a coordinate which is out of the boundry of image.
    m = len(image[0])     

    # Creating a function to carry out our recursively functionality
    def helper(image,i,j,newColor,oldColor,n,m):
        
        # Im going to change given coordinates value to the 
        # new Value.
        image[i][j] = newColor

        # Then im going to check the adjacent coorinates and see
        # if there value match the given coordinates value

        # Im going to make recursive calls for each adjacent
        # coordinate as well so then I can look at there
        # adjacent coordinates and see if there values match the 
        # given coordinates value as well. and if it does we
        # change there value and make recursive calls through
        # them as well
        
        # We keep doing this until we reach to a point where
        # there are no adjacent coordinates whose values are equal 
        # to given value


        # We only make a recursive call to change adjacent 
        # coordinates value to new value only if:

        # 1) If the adjcant coordinate actually exist
         
        # 2) If the adjacent coordinates current value is equal
        # to the given coordinates value.

        # CHECKING THE GIVEN CONDITIONS FOR ALL THE ADJACENT
        # NODES.

        # First check if a adjacent coordinate above my current
        # coordinate actually exist. 

        # Why cause my given coordinate might be on the 1st row 
        # itself so there wont be a adjacent coordinate on the top.

        # Second thing I check if the adjacent coordinates value
        # is equal to the given coordinates value cause only then
        # I can make the recursive call to change its value to 
        # the new value

        if i+1 < n and image[i+1][j] == oldColor:
            helper(image,i+1,y,newColor,oldColor,n,m)

        # First check if a adjacent coordinate below my current
        # coordinate actually exist 
        
        # Cause my current coordinate might be on the last row 
        # itself so there wont be a adjacent coordinate below it
        
        # Second thing I need to check if the adjacent coordinates
        # value is equal to the given coordinate cause only then I
        # can make a recursive call for it to change its value to
        # the new value

        if i-1 >= 0 and image[i-1][j] == oldColor:
            helper(image,i-1,j,newColor,oldColor,n,m)

        # First check to see if a adjacent coordinate on the right
        # of the current coordinate actually exist. 
        
        # Cause my current coordinate might be on the last column
        # itself so is no adjacent coordinate on its right so i
        # need to check that.

        # Second check would be to check if the adjacent coordinates
        # value is equal to given coordinate cause only then I can
        # make recursive call to change its value to new value
        
        if j+1 < m and image[i][j+1] == oldColor:
            helper(image,i,j+1,newColor,oldColor,n,m)
        
        # First check to see if a adjacent coordinate on the left
        # actually exist 

        # Cause the current coordinate might be on the first row
        # so in that case there would be no coordinate on the left.

        # Second check would be to check if the adjacent coordinates
        # value is equal to given coordinates value cuase only then
        # I can make a recursive call to change its value to the new
        # value

        if j-1 >= 0 and image[i][j-1] == oldColor:
            helper(image,i,j-1,newColor,oldColor,n,m)

    helper(image,x,y,newColor,oldColor,n,m)
    return image

print(flood_fill_algorithm(image,1,2,8))

