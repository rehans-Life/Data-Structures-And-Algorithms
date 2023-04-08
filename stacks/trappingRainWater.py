def trappingRainWater(elevations):
    
    n = len(elevations)
    waterStored = [0] * n
    
    # To find the max height bar from the left of each element.
    for i in range(n):
        if i-1 < 0:
            waterStored[i] = elevations[i]
        elif waterStored[i-1] >= elevations[i]:
            waterStored[i] = waterStored[i-1]
        elif waterStored[i-1] < elevations[i]:
            waterStored[i] = elevations[i]
            
    # To find the max height bar from the right of each elemnt
    # And if its smaller then im replacing it in the array.
    for j in reversed(range(n)):
        if j+1 >= n:
            waterStored[j] = min(waterStored[j],elevations[j])
        elif waterStored[j+1] > elevations[j]:
            waterStored[j] = min(waterStored[j],waterStored[j+1])
        elif waterStored[j+1] <= elevations[j]:
            waterStored[j] = min(waterStored[j],elevations[j])
            
    # Subtracting the current bars height from min of the left
    # and the right max to get the water stored at that bar.
    for i,height in enumerate(elevations):
        waterStored[i]-=height

    # Returning the sumation of units of water stored.
    return sum(waterStored)

arr = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trappingRainWater(arr))