def move_negative(arr):
    i = 0 
    for j,num in enumerate(arr):
        if num < 0:
            temp = arr[i]
            arr[i] = num
            arr[j] = temp
            i+=1
    return arr
print(move_negative([-4,2,1,3,5,6,-2,4,-4,-2]))