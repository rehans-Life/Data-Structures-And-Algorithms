import heapq

def kLargest(self,arr, n, k):
		heap = []
		heapq.heapify(heap)
		
		for num in arr:
		    heapq.heappush(heap,num)
		    
			if len(heap) > k:
a				heapq.heappop(heap)
		
		heap.sort(reverse=True)
		return heap
