# Creating a class node which is a representation of a node in a doubly linked list since we are going to be storing a doubly
# linked list at each index. A node in a doubly linked list is initialized a value attribute to store the node's value, a next
# attribute which is initially empty but when a node is added then this next attribute stores that nodes reference, a prev attribute
# which stores a reference to the node which exists behind this node.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str({
            'value':self.value,
            'next':self.next,
            'prev':self.prev
        })

class Hashset:
    # Our hashset is initialized with a 11 size array where each element is initially is filled with a zero.
    def __init__(self):
        self.set = [0] * 11
    def hash(self,key):
    # A hash function which is going to generate an index for the value to be added to set with in the array. We are using a simple 
    # hash function which is just a modulo of that number with the length of the array which is going to give us a number between 0 to
    # one less than the length of the array. So we can then use that index within the array to represent that value.
        return key % len(self.set)
    def add(self,key):
    
    # If that key is already in the set then we exit the function directly cause a set is a data structure which stores unique elements.
        if self.contains(key):
            return
    
    # So first we find the index which represents this value in our array using the hash function.
        index = self.hash(key)

    # We are creating a node with the value as of our key.
        node = Node(key)

    # We check if that place is empty or not
        if self.set[index] == 0:
            # If it is empty then we intiating a linked list at that index with the node we just created as its head node.
            self.set[index] = node
    
    # If there is already a linked list then i add this node at the end of our linked list which is at that index.
        else:
            # We get the head of our linked list by accessing that particular because the head node is always at the top.
            head = self.set[index]

            # I create a temporary variable which is initialized with a the head of the linked list but keeps on changing as we iterate
            # through the linked list
            temp = head
            while True:
                # When i find the last node of our linked list then i can check that by checking if the node is pointing towards none
                # or not. If it is then its the last node now in our last node i need to sets its next attribute to point towards
                # the new node that we created and we set our new nodes previous atttribute to point towards this current last node
                # of our linked list.

                if temp.next == None:
                    temp.next = node
                    node.prev = temp
                    break

                # We keep changing the nodes until we get to the end of the node.
                temp = temp.next

    def remove(self,key):
        # If that key doesnt exist then we return -1.
        if not self.contains(key):
            return -1
        # So if the key exists then we find the index where this key exists.
        index = self.hash(key)
        head = self.set[index]
        # Then we create a temporary variable initialized with the head of the linked lists but will keep on changing as we traverse
        # through the linked list.
        temp = head
        while temp != None:
            # After we find that node which represents this key in our linked list and again we can find the node which represents the
            # key by checking if the nodes value attribute is equal to that particular key or not.
            if temp.value == key:
                if temp.prev == None:
                    # Deleting the first node from the linked list. we can check if the node is the head node if its prev attribute is 
                    # set to none.
                    if temp.next != None:
                        # Setting the head node as the node which is next to our current head node since we deleting our current head
                        # node.
                        self.set[index] = temp.next
                        # Then setting the previous attribute of the next node to our current head node to None since its the head now.
                        temp.next.prev = None
                    else:
                        # If there was only one node then i set that index to 0
                        self.set[index] = 0
                    # Then deleting the head node from memory.
                    del temp
                elif temp.next == None:
                    # Deleting the last node in our linked list. We can check if the node is the last node if its next attribute is 
                    # set to none.
                    temp.prev.next = None
                    del temp
                else:
                    # When the node to be deleted is somewhere in the middle of the linked list.
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    del temp
                break
            temp = temp.next
    def contains(self,key):
        # First finding the index of the key as to where it should exist in the array.
        index = self.hash(key)

        # If there is nothing at that index then i return False directly cause that spot is empty which means there is no key here.
        if self.set[index] == 0:
            return False

        # If there is a something there at that index then thats a linked list now i need to traverse through the linked list and try to
        # find the node which stores this key in there value attribute
        head = self.set[index]
        temp = head
        while temp != None:
            # When we find the node whose value attribute is the same as the key that we wanted to exists then we return True cause this
            # would mean its does exists
            if temp.value == key:
                return True
            temp = temp.next
        # Now if we traversed through the whole linked list without finding the node which represents our key then that means the key
        # doesnt exist so we return False.
        return False

myHashSet = Hashset()
myHashSet.add(0)
myHashSet.add(11)
myHashSet.add(22)
myHashSet.remove(0)
print(myHashSet.contains(0))
print(myHashSet.set[0])