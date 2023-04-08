# Optimal

# Time Complexity: O(n1+n2+n3)
# Space Complexity: O(n)

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        
        # We will have three pointers this time 
        # Our x pointer is going to be for array A
        # Our y pointer is going to be for array B
        # Our z pointer is going to be fore array C
        x = y = z = 0
        
        # An array which is going to store our common elements b/w A, B and C
        result = list()
        
        # Iterating through all the arrays at once until we finish our iteration 
        # for one of the arrays cause then that means if we iterate through the
        # remaining elements in the other arrays we are only going to get elements
        # which are greater than the elements which we finished traversing and hence
        # they will not considered as common elements
        while x < n1 and y < n2 and z < n3:
            
            # If the elements to which my x, y and z pointers are pointing at 
            # in my A, B and C arrays respectively are equal thats means that
            # value is the intersecting element so we append it to our answer
            # incrementing all counters by one
            if A[x] == B[y] and B[y] == C[z]:
                result.append(A[x])
                
                # These while loops are making sure we skip instances of the common
                # element after have added it to our list.
                temp = A[x]
                while x < n1 and temp == A[x]:
                    x+=1
                temp = B[y]
                while y < n2 and temp == B[y]:
                    y+=1
                temp = C[z]
                while z < n3 and temp == C[z]:
                    z+=1
            
            # If a is less than either of the elements then we incrementing it 
            # accordingly.
            elif A[x] < B[y] or A[x] < C[z]:
                temp = A[x]
                while x < n1 and temp == A[x]:
                    x+=1
            elif B[y] < A[x] or B[y] < C[z]:
                temp = B[y]
                while y < n2 and temp == B[y]:
                    y+=1
            elif C[z] < A[x] or C[z] < B[y]:
                temp = C[z]
                while z < n3 and temp == C[z]:
                    z+=1
            
        return result