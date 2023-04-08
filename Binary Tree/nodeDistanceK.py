from typing import List
from queue import Queue

class Node:
    def __init__(self,val: int,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
root = Node(1)
root1 = Node(2)
root2 = Node(3)
root3 = Node(4)
root4 = Node(5)
root5 = Node(8)
root6 = Node(6)
root7 = Node(7)
root8 = Node(9)
root9 = Node(10)
root.left = root1
root.right = root2
root1.left = root3
root1.right = root4
root4.left = root5
root2.left = root6
root2.right = root7
root7.left = root8
root7.right = root9

def distanceK(root: Node, target: Node, k: int) -> List[int]:

        # Doing a bfs traversel to get the parent pointers for each node which we are going to 
        # store inside of our hashmap.
        parent = dict()

        # A queue for our level order traversel.
        queue = Queue()

        queue.put(root)

        while not queue.empty():
            node = queue.get()

            # Mapping the child nodes of the current node that im traversing to its children
            # so that we can have parent pointers then.

            if node.left:
                queue.put(node.left)
                parent[node.left] = node
            
            if node.right:
                queue.put(node.right)
                parent[node.right] = node

        # Now running a BFS going outwards from all directions from each starting from the 
        # target node.
        queue = Queue()

        # Maintaining a visited hashset so we dont visit the same nodes again
        visited = set()

        # Maintaining a distance variable to store the distance of the nodes from my target
        # node that im traversing so that i know how far the nodes aren and accordinly stop when the
        # nodes are at a distance of two.
        distance = 0

        queue.put(target)

        while not queue.empty():
            qSize = queue.qsize()

            if distance == k:
                break

            for i in range(qSize):

                node = queue.get()
                visited.add(node)

                if node in parent and parent[node] not in visited:
                    queue.put(parent[node])

                if node.left and node.left not in visited:
                    queue.put(node.left)
                
                if node.right and node.right not in visited:
                    queue.put(node.right)

            distance+=1  

        ans = list()
        while not queue.empty(): ans.append(queue.get().val)            

        return ans
    
print(distanceK(root,root4,5))