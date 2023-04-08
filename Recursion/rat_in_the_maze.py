arr = [
    [1, 0, 0, 0], 
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
n = 4
def maze(arr,n):
    visited = set()
    ans=[]
    def helper(x,y,path=[]):
        
        # This is going to stop me from going in the wrong direction.
        if x < 0 or y < 0 or x >= n or y >= n or (x,y) in visited or arr[x][y] == 0:
            return
        
        # Stop after I have reached my destination and I append the path that Ive taken to get to that location
        # to my asnwer array.
        if x == n-1 and y == n-1:
            ans.append(''.join(path))
            return
        
        # If im going in the correct direction then i add the coordinate in my visited set so i dont visit it again. 
        visited.add((x,y))


        # Going towards the downwards direction from our current coordinate so appending D to my path
        path.append('D')
        helper(x+1,y,path)

        # Removing D from the path cause im going to take a different path now from our current coordinate.
        path.pop()

        # Appending L to my path cause im going to take the left path now from my current coorinate
        path.append('L')
        helper(x,y-1,path)

        # After finishing visisting the left direction I pop L out cause im going to be taking a different now from
        # my current coordinate
        path.pop()

        # Going to the Right direction now from my current cooridinate so I append R to my path
        path.append('R')
        helper(x,y+1,path)

        # After finishing visiting the right side I pop out R from the path cause im going to taking a different
        # direction from my current coordinate.
        path.pop()

        # Going to the upward direction from my current coordinate so i append U to my path.
        path.append('U')
        helper(x-1,y,path)

        # After finishing the upward side i pop out U from the path.
        path.pop()

        # After I have finished generating paths from this particular coordinate then ill backtrack and remove the coorinates used to
        # create these paths so I that im able to generate other paths as well which use similar coordinates to get to the destination. 
        visited.remove((x,y))

    helper(0,0)
    return ans

print(maze(arr,n))