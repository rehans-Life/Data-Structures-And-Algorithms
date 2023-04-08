#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Sorting the array to be able to create 
        A.sort()
        for i in range(n):
            l = i+1
            r = n-1
            while (l < r):
                tripletSum = A[i] + A[l] + A[r] 
                if tripletSum == X:
                    return True
                elif tripletSum > X:
                    r-=1
                else:
                    l+=1
        return False