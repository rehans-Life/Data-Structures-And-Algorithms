def implementI(n,edges):
    adjacencyMatrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for x,y,z in edges:
        adjacencyMatrix[x][y] = z
        adjacencyMatrix[y][x] = z
        
    return adjacencyMatrix

def implementII(n,edges):
    adjacencyList = [[] for _ in range(n+1)]
    
    for x,y,z in edges:
        adjacencyList[x].append([y,z])
        adjacencyList[y].append([x,z])

    return adjacencyList

edges = [[1,2,5],[1,3,10],[2,4,7],[3,4,7],[3,5,1],[4,5,6]]

print(implementI(5,edges))
print(implementII(5,edges))