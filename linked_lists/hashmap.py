# A Hashmap is data structure stores key value pairs where key are 
# addresses in the memory again whom there corresponding values are
# are stored.

# We can very easily represent it through an array and whenever tries to
# insert we set the index equal to that as the value itself.
import math

class Hashmap:
    def __init__(self):
        self.map = [-1] * math.floor(1e6)
    
    def add(self,key,value):
        self.map[key] = value
    
    def remove(self,key):
        self.map[key] = -1
    
    def get(self,key):
        return self.map[key]
    
myHashmap = Hashmap()

myHashmap.add(10,43)
myHashmap.add(19,23)
myHashmap.add(8,12)
myHashmap.remove(19)
myHashmap.add(19,90)
print(myHashmap.get(8))
print(myHashmap.map[0:20])