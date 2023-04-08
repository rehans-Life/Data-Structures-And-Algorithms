from heapq import *
def getKthLargest(arr, k):

	# A min heap of size which is going to store the subarray sums and maintain a 
	# size of k
	heap = []
	heapify(heap)

	# Generating all the subarray sums and inserting them into the heap
	for i in range(len(arr)):
		currSum = 0
		for j in range(i,len(arr)):
			currSum+=arr[j]
			# Adding the new subarray sum generated into the heap
			heappush(heap,currSum)
			# If after inserting the size of the heap has become k+1 that means
			# the root subarray sum is smaller than k other sums therefore it can
			# never be our answer so we pop it out
			if len(heap) == k+1: 
				heappop(heap)
	
	# In the end our heap will be of size k and the root sum will be the kth
	# largest subarray sum of the array.
	return heappop(heap)