from string import ascii_letters,ascii_lowercase

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
    
    def containsKey(self,char: str) -> bool:
        return self.links[ascii_letters.index(char)]
    
    def insertKey(self,char: str,trieNode: 'TrieNode'):
        self.links[ascii_letters.index(char)] = trieNode 
    
    def getRefNode(self,char: str):
        return self.links[ascii_letters.index(char)]

    def setEnd(self):
        self.flag = True
    
    def getFlag(self):
        return self.flag
    
    def getLinks(self):
        return self.links

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word: str):
        
        node = self.root

        for char in word:

            if not node.containsKey(char):
                node.insertKey(char,TrieNode())

            node = node.getRefNode(char)
        
        node.setEnd()
    
    def getSuggestions(self,prefix,curr,output):
        
        if curr.getFlag():
            output.append(prefix)
        
        for char in ascii_lowercase:
            if char and curr.containsKey(char):
                temp = prefix
                prefix = prefix + char
                self.getSuggestions(prefix,curr.getRefNode(char),output)
                prefix = temp
                

def phoneDirectory(arr,qList):
    trie = Trie()
    output = []
    prefix = ""
    prev = trie.root
    
    # Insert all contacts into the trie data structure
    for contact in arr:
        trie.insert(contact)

    # Taking each prefix of our query and checking if there are words
    # that exists with it and if there are we add them to our output array
    for char in qList:
        
        if not prev.containsKey(char):
            break

        prefix = prefix + char 
        prev = prev.getRefNode(char)
        trie.getSuggestions(prefix,prev,output)

    return output

arr = ['geeikistest','geeksforgeeks','geeksfortest']
query = 'geeips'
print(phoneDirectory(arr,query))
