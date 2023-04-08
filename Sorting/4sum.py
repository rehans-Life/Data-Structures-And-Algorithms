def fourSum(arr,n,target):
    
    arr.sort()
    res = list()
    i = 0
    while i < n:
        j = i+1
        while j < n:
            target1 = arr[i]+arr[j]
            target2 = target - target1
            
            left = j+1
            right = n-1
            
            while left < right:
                sum_2 = arr[left] + arr[right]
                if sum_2 < target2:
                    temp = arr[left]
                    while arr[left] == temp: 
                        left+=1
                elif sum_2 > target2:
                    temp = arr[right]
                    while arr[right] == temp:
                        right-=1
                else:
                    quad = list()
                    quad.append(arr[i])
                    quad.append(arr[j])
                    quad.append(arr[left])
                    quad.append(arr[right])
                    res.append(quad)
                    
                    temp = arr[left]
                    while arr[left] == temp: 
                        left+=1
                        
                    temp = arr[right]
                    while arr[right] == temp:
                        right-=1
                                    
            temp = arr[j]            
            while j < n and temp == arr[j]:
                j+=1
        temp = arr[i]
        while i < n and temp == arr[i]:
            i+=1
        
    return res

arr = [10,2,3,4,5,7,8]
print(fourSum(arr,len(arr),23))
            