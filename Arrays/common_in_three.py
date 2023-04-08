# Brute Force 

# Space Complexity: O(n)
# Time Complexity: O(n1+n2)

#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        
        # Result is going to store the intersecting elements between all three arrays
        
        # While temp is going to store the intersecting elements between A and B array
        result = list() 
        temp = list()
        
        # Our ith pointer is going to traverse through the array A
        i = 0
        # Our jth pointer is going to traverse through the array B
        j = 0
        
        # We keep iterating until we have iterated completely through one of the arrays
        while i < n1 and j < n2:
            # Three Conditions can exist.
            
            # Case 1: could be when our ith element is less than our jth element
            # if thats the case then the ith element from Array A doesnt exist 
            # in our array B. 
            
            # Hence we shift the i pointer only cause since jth element was more 
            # than our ith element hence when shift i pointer and since the array is
            # sorted we are going ot be pointing to a element greater than our current
            # i value hence there could be a chance we end up pointing at an element
            # equal to our jth element so we dont shift j.
            
            if A[i] < B[j]:
                tempI = A[i]
                
                # Dont be confused this loop makes sure we skip all instances of 
                # our ith element from our array since there could be repeating 
                # elements in the array.
                
                # So we have to make sure are skipping elements whose value is 
                # equal to i and since array is sorted all of the instances exist
                # next to each other.
                while i < n1 and tempI == A[i]:
                    i+=1
            
            # Case 2 : Our jth element in array B is less than our ith element in 
            # array A this means our jth element doesnt exist in our Array A hence
            # we increment j pointer
            
            # But we dont increment i pointer since ith element was greater than j
            # and this is a sorted array then there are chances that we might end up
            # pointing at an element in Array B by incrementing j whose value is 
            # equal to ith element since i was greater and by increasing j we will
            # pointing at an element greater than it.
            
            elif A[i] > B[j]:
                tempJ = B[j]
                
                # Again to skip all instances of the jth element
                while j < n2 and tempJ == B[j]:
                    j+=1
            
            # Now else is when they are both equal so in that case thats the common 
            # element hence we add it to our temporary answer and we increment both
            # the answers.
            else:
                temp.append(A[i])
                temp1 = A[i]
                i+=1
                while i < n1 and temp == A[i]:
                    i+=1
                temp2 = B[j]
                j+=1
                while j < n2 and temp2 == B[j]:
                    j+=1
            
        # Now we take the array A and array B's intersecting elements and we find 
        # which of them exists inside of Array C also then we will finally get the 
        # intersecting elements between our Array A, Array B and Array C
        
        # Againing initializing pointers for both the arrays.
        i = j = 0
        t = len(temp)
        while i < n3 and j < t:
            
            if C[i] < temp[j]:
                tempI = C[i]
                i+=1
                while i < n1 and tempI == C[i]:
                    i+=1
            
            elif temp[j] < C[i]:
                tempJ = temp[j]
                j+=1
                while j < t and tempJ == temp[j]:
                    j+=1
            
            else:
                result.append(temp[j])
                tempJ = temp[j]
                j+=1
                while j < t and tempJ == temp[j]:
                    j+=1
                tempI = C[i]
                i+=1
                while i < n3 and tempI == C[i]:
                    i+=1
                
        return result
        
