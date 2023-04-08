from queue import Queue
class Solution:    
    def isCyclic(self, V, adj):
        
        # An array to mark our visited nodes in general
        visited = [False] * V
        
        # An array to mark the nodes that ive visited in my current path
        pathVisited = [False] * V
        
        # A dfs recursive function
        def helper(node):
            
            # Marking the node im traversing as visited and since im on it hence its in my path as well
            visited[node] = True
            pathVisited[node] = True
            
            # Then going in dept into all of its unvisited neighbours
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    # If the neighbour found a cycle hence we return
                    # a True.
                    if helper(neighbour):
                        return True
                # If the neighbour is visited as well as its in my path already that means im traversing it the 
                # second so i can return True.
                elif pathVisited[neighbour]:
                    return True
            
            # Then if i dont get any cycles by going into all the paths hence I can return False and i can remove it 
            # from the path as well cause im backtracking from it.
            pathVisited[node] = False
            return False
            
        # The graph could be divided into connected components.
        # So i need to traverse all the components and check if there
        # is a cycle
        for i in range(V):
            # If node not visited hence its a part of a component
            # i havent traversed and checked so i will perform the 
            # dfs on it and check if its has a cycle
            if not visited[i]:
                if helper(i):
                    return True
                    
        # If none of the components have cycle then i return False
        return False
        
def detectCycleInDirectedGraph(n, edges):
        # A queue for our in bfs traversel
        queue = Queue()
        
        # An array which is going to store the indegrees of each node
        # indegrees means the number of edges coming into a node
        indegrees = [0] * n
        
        ans = []
        
        # Iterating through the nodes and checking which nodes adjacency
        # list contains the node and if it does we increment the indegree
        # count for the node.
        for node in range(n):
            for i in range(n):
                if node in edges[i]:
                    indegrees[node]+=1
        
        # Then i know the nodes which have zero indegree will come in
        # start of the ordering hence i include initially into the stack
        # so that they are placed first cause there is no need that
        # needs to exist before them.
        for node in range(n):
            if indegrees[node] == 0:
                queue.put(node)
        
        # Iterating until queue is empty
        while not queue.empty():
            # Taking the top most node out and inserting it into the
            # ordering cause ive already placed all the nodes that 
            # should exist on the left of it in the ordering already
            node = queue.get()
            
            ans.append(node)
            
            # Then since ive inserted this node then the nodes to
            # which it has an outward edge to there indegrees should be
            # reduced cause one of the nodes should on the left of
            # them is placed and if this was the last one left hence
            # those guys will be added to queue then to be placed in the
            # ordering
            for neighbour in edges[node]:
                indegrees[neighbour]-=1
                if indegrees[neighbour] == 0:
                    queue.put(neighbour)
            
        # Now how do i check if this graph has cycle or not through
        # all of this because a valud topo ordering is only possible on
        # a DAG which means if this graph has a cycle then i wont be
        # able to create a valid ordering
        
        # So if the ordering size is equal to the number of nodes 
        # present in the graph then there is no cycle cause the ordering
        # is valid then but if not equal to V then cycle exists thats
        # why i couldnt create a complete linear ordering
        
        return False if len(ans) ==  n else True