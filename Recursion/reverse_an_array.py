# Reverse an array Using recursion.

def reverse(array):

    # Base Case is that if the function gets called with 
    # an array which has a length of one we return the same array.

    if len(array) == 1:
        return array

    # The formula is that if i am able to find the reverse of 
    # the array without the first element and then i can just 
    # append the first element to the that reversed array which
    # is going to give us the reverse of the whole array.

    # Finding the reverse the array without first element
    slicedReversedArray = reverse(array[1:])

    # Appending the first element
    slicedReversedArray.append(array[0])

    # Returning the reversed array.
    return slicedReversedArray

print(reverse([1,2,3,4,5,6,7,8,9,10]))