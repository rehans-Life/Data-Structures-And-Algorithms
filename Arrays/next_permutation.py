class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 1:
            return nums

        # Index of the item that needs to be modified in order to generate our new permutation.
        index1 = -1

        # For this we need to iterate through the array in reverse and the first element which is 
        # less than the element infront of it is the element is the item we need to replace.
        for i in reversed(range(0,n-1)):
            if nums[i] < nums[i+1]:
                index1=i
                break

        if index1 < 0:    
            nums.reverse()
            return nums
        
        # Index of the item thats next in the sequence to replace the item in the index1 position
        # this element is always going to be the first element that is greater than the index1
        # element in the decreasing order.
        index2 = 0 

        for i in reversed(range(0,n)):
            if nums[i] > nums[index1]:
                index2 = i
                break
        
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        # Swapping the values of index1 and index2 since in order to generate the next permutation
        # we need to have the element at index2 take place of the element at index1
        swap(index1,index2)

        # Reversing the decreasing order into the increasing order in order to get the first permutation
        # of the item at index1

        s = index1+1
        e = len(nums)-1

        while s < e:
            swap(s,e)
            s+=1
            e-=1

        return nums