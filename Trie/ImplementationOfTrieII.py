from os import *
from sys import *
from collections import *
from math import *
import string

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.endsWith = 0
        self.countPrefix = 0
    
    def containsKey(self,char: str) -> bool:
        return self.links[string.ascii_letters.index(char)]
    
    def insertKey(self,char,trieNode):
        self.links[string.ascii_letters.index(char)] = trieNode

    def incrementPrefix(self):
        self.countPrefix+=1
    
    def getRefNode(self,char):
        return self.links[string.ascii_letters.index(char)]
    
    def incrementEnd(self):
        self.endsWith+=1
    
    def endCount(self) -> int:
        return self.endsWith
    
    def prefixCount(self) -> int:
        return self.countPrefix

    def decrementPrefix(self):
        self.countPrefix-=1
    
    def decrementEnd(self):
        self.endsWith-=1

class Trie:
    def __init__(self):
        # Write your code here.
        self.root = TrieNode()

    def insert(self, word):
        # Write your code here.
        node = self.root

        for i in range(len(word)):
            char = word[i]

            if not node.containsKey(char):
                node.insertKey(char,TrieNode())

            node = node.getRefNode(char)
            node.incrementPrefix()
        
        node.incrementEnd()

    def countWordsEqualTo(self, word):
        node = self.root

        for i in range(len(word)):
            char = word[i]

            if not node.containsKey(char):
                return 0
            
            node = node.getRefNode(char)
        
        return node.endCount()

    def countWordsStartingWith(self, word):
        node = self.root

        for i in range(len(word)):
            char = word[i]

            if not node.containsKey(char):
                return 0

            node = node.getRefNode(char)
        
        return node.prefixCount()

    def erase(self, word):
        # Write your code here.
        node = self.root

        for i in range(len(word)):
            char = word[i]

            node = node.getRefNode(char)
            node.decrementPrefix()        

        node.decrementEnd()
