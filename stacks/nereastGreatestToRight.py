class Solution:
    def nextLargerElement(self,arr,n):
        
        # Creating a stack to store the elements to the right of a certain
        # element and stack will store them in order as well
        stack = list()
        
        # Maintaining an output array of size n to store the ouput
        # for each element
        output = [0] * n
        
        # Running a reverse loop on the array and finding the next
        # greatest integer from the right to left
        
        for i in reversed(range(n)):
            
            # If stack's length is zero hence there are no elements to
            # the right side of the element which are greater than it
            if len(stack) == 0:
                output[i] = -1
            elif stack[len(stack)-1] > arr[i]:
                # If the top element of stack is greater than its the
                # nearest greatest integers on the right of my current
                # element
                output[i] = stack[len(stack)-1]
            else:
                # If top element is not greater than we have to keep
                # removing elements from the top of the stack until 
                # we find one 
                
                while len(stack) > 0 and stack[len(stack)-1] <= arr[i]:
                    stack.pop()
                    
                # When this loop ends then either we have found a 
                # element greater than current element or we emptied 
                # the stack cause there were no elements greater than
                # current element.
                
                if len(stack) == 0:
                    output[i] = -1
                else:
                    output[i] = stack[len(stack)-1]
            
            # We add the element in stack 
            stack.append(arr[i])
        
        return output