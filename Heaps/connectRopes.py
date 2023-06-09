from heapq import *
def connectRopes( arr, n) :
	# A min heap to store our ropes in order from smallest to largest lengths
	heap = []
	heapify(heap)

	# Acculator for costs to sum all the ropes
	cost = 0

	# Insert all the ropes into the minHeap
	for rope in arr: heappush(heap,rope)

	# Then running an iteration until heap has only one rope inside of it
	while len(heap) > 1:
		# We take the two smallest ropes upon each iteration sum there lengths 
		# to find the cost of addition of ropes and the length of the new rope
		s1 = heappop(heap)
		s2 = heappop(heap)

		sum = s1+s2

		# Adding the cost it took to combine the two ropes into the accumulator
		cost+=sum

		# Inserting the new rope generated by combining the two ropes back into 
		# the heap
		heappush(heap,sum)

	return cost
