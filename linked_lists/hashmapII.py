# In Approach we will be using a size of a fixed size in the 
# implementation previously we created an array with size equal to the 
# maxiumum key value of the array.

# Since array is of fixed size we will be using a hash function to 
# generate an index for a key value pair on the array.

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
    
    def __str__(self):
        return str({
            'key':self.key,
            'value':self.value,
            'next':self.next,
            'prev':self.prev
        })

class Hashmap:
    def __init__(self):
        self.map = [-1] * 10
    
    def hash(self,key):
        return key % len(self.map)

    # Search function searches for the node with the given key and
    # returns the node
    def search(self,key):
        # First we need to find at what index will the node related 
        # to this key will be located.
        index = self.hash(key)

        head = self.map[index]

        if self.map[index] == -1:
            return None

        temp = head

        # Iterating through the linked list at that index to find 
        # the node with represents the given key
        while temp != None:

            # When we find that node we return that node
            if temp.key == key:
                return temp

            temp = temp.next
        
        # If we are not able to find we return None
        return None
    
    def put(self,key,value):

        # First we find the index as to where we should place this 
        # key value pair on the array. And we use the hash function
        # for it.

        index = self.hash(key)

        # Checking to see if a node already exists with the given key
        # or not
        searchedNode = self.search(key)

        # If it does then we just update the value attribute of that 
        # node to the new value
        if searchedNode != None:
            searchedNode.value = value
        
        # If not then we create a new node with the given key and append
        # it to the index.
        else:

            # Creating a node for representing the key value pair on the
            # array.
            node = Node(key,value)

            # Case where there are no previous key value pairs stored on 
            # the index

            if self.map[index] == -1:

                # If there is no other key value pair then I create a linked 
                # list at that index with the new node being the head node.
                self.map[index] = node

            else:
                # if there are already key value pairs there then we that means
                # there is a linked list present at the index therefore
                # we have to add our key value pair Node at the end of the
                # linked list.
                
                head = self.map[index]

                temp = head

                while True:

                    if temp.next == None:

                        # When we find the last im going to set its next
                        # attribute to the new node we just created cause
                        # we have to add the new node infront of this prev
                        # last node 
                        temp.next = node

                        # Also since this is a doubly linked list I
                        # need to add a reference to this last node 
                        # in the my new node's prev attribute.
                        node.prev = temp
                        break
                    
                    temp = temp.next

    def get(self,key):

        # We search if a node with the given key exists or not
        searchNode = self.search(key)                

        # If it does we return the value associated with it through
        # the value attribute.
        if searchNode != None:
            return searchNode.value
        # If not we return -1.
        else:
            return -1
    
    def remove(self,key):

        # Finding the reference to the node with the given key.
        node = self.search(key)
        index = self.hash(key)

        # If we find the node we delete it now.
        if node != None:
            
            # First checking to see if the node to be deleted is the 
            # head node or not.
            if node.prev == None:
                if node.next == None:
                    self.map[index] = -1
                else:
                    self.map[index] = node.next
                    node.next.prev = None
                del node
            # If the node to be deleted is ladt node
            elif node.next == None:
                node.prev.next = None
                del node
            # If the node to be deleted is somewhere in the middle
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                del node
            
myHashmap = Hashmap()

myHashmap.put(20,2445)
myHashmap.remove(20)
print(myHashmap.map[0])