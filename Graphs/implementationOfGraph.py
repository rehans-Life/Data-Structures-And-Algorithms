# Adjacent Matrix.

# Space Complexity for this Approach => O(n*n)
# Time Complexity for this Approach => O(m)

def implementI(n,m,edges):
    
    adjacencyMatrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for x,y in edges:
        adjacencyMatrix[x][y] = 1
        adjacencyMatrix[y][x] = 1
        
    return adjacencyMatrix

print(implementI(5,5,[[1,2],[1,3],[2,4],[3,4],[3,5],[4,5]]))

# Adjacency List.

# Space Complexity: O(2*Edges in the graph) 
# Why because for each edge that we have in our graph we are storing two elements cause its a two way edge
# In directed grpah the space would be only k cause one edge points at one element only.

# Time Complexity: o(Number of edges)

def implementII(n,edges):
    
    # Here one thing we know that the value of nodes in the graph is from 1 to n.
    # Hence we create an array of size n+1 so that we have an index representing 
    # each value in the graph and at each index we place an array to store the 
    # value of nodes which are connected to it via an edge
    adjacencyList = [[] for _ in range(n+1)] 
    
    for x,y in edges:
        # Since the edges are bidirectional hence its a two way edge which connects them both to each 
        # other so add there values to the array. 
        adjacencyList[x].append(y)
        adjacencyList[y].append(x)
         
    return adjacencyList

print(implementII(5,[[1,2],[1,3],[2,4],[3,4],[3,5],[4,5]]))        