from queue import Queue

def bfs(v: int,adj: list[list[int]]):
    # A queue which is going to store the neighbouring nodes of the nodes we are currently traversing.
    queue = Queue()
    
    # A visited array which is going to mark the nodes we have already visited its going to be of size v to cover
    # all node values present in the array
    visited = [False] * v
    
    # A list to store our bfs traversel nodes
    bfs = []
    
    # Initially including our starting node inside of the queue and marking it as visited
    queue.put(0)
    visited[0] = True
    
    while not queue.empty():
        # Taking the top most node out of the queue and including it in our traversel
        node = queue.get()
        bfs.append(node)
        
        # Then inserting the neighbouring nodes inside of the queue for the next level's traversel only if they are
        # not already visited
        for neighbour in adj[node]:
            if not visited[neighbour]:
                queue.put(neighbour)
                # Then marking the neighbour as visited
                visited[neighbour] = True
    
    return bfs
        