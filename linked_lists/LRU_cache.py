class Node:
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None
    
class LRUCache:
    def __init__(self,capicity):

        # This is the hashmap that is going to store the keys mapped
        # to the addresses of the nodes that represent them in the 
        # linked lists
        self.cache = dict()

        # The amount of key value pairs we can add to our cahce
        self.cap = capicity

        ''' 
        Setting up the Linked Lists for determing our most and 
        least recently used nodes.
        '''

        # This is the left dummy node of the linked lists
        self.left = Node()

        # This is the right dummy node of the linkeds
        self.right = Node()

        # Connecting these dummy nodes
        
        # The reason why im connecting them is cause im going to insert
        # my nodes in between these two dummy nodes
        self.left.next,self.right.prev = self.right,self.left

    def remove(self,node):
        prev,nxt = node.prev,node.nxt
        prev.nxt,nxt.prev = nxt,prev

    def insert(self,node):
        prev,nxt = self.left,self.left.nxt
        node.prev,node.nxt = prev,nxt
        prev.nxt = nxt.prev = node 

    def get(self,key):

    # Checking to see if the key exists 
        if key in self.cache:

            # Removing the node that represents this key from the
            # linked lists
            self.remove(self.cache[key])

            # Then inserting it in the beginning of the linked lists
            self.insert(self.cache[key])    

            # If it does exist we return the value from the node.
            return self.cache[key].val
        
        else:
            # If it doesnt we return -1
            return -1
    
    def put(self,key,value):

        # We first check if a key value pair already exists with the
        # given key.
        if key in self.cache:
          
            # If it does then we remove its node from the linked lists
            self.remove(self.cache[key])
        
        # Creating a new node with the new value
        self.cache[key] = Node(key,value)

        # Inserting the new node in the beginning of the linked lists
        self.insert(self.cache[key])

        # Checking if we have gone over the capacity
        if len(self.cache) > self.cap:

            # We need to delete our least recently used data both
            # from the linked lists and the hashmap

            # The least recently used data is in the end of the linked
            # lists which is the node previous to the right dummy
            # node.
            
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]

             
