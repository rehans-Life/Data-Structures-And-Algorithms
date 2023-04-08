from os import *
from sys import *
from collections import *
from math import *

from typing import List

from string import ascii_letters,ascii_lowercase


class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.wordEnd = 0
        self.isSpace = None
    
    def isSpaceExist(self) -> bool:
        return False if not self.isSpace else True
    
    def createSpace(self,trieNode: 'TrieNode') -> None:
        self.isSpace = trieNode
    
    def containsKey(self,char: str) -> bool:
        return self.links[ascii_letters.index(char)] 
    
    def insertKey(self,char: str,trieNode: 'TrieNode') -> None:
        self.links[ascii_letters.index(char)] = trieNode
        
    def getRefNode(self,char: str) -> 'TrieNode':
        if char == ' ':
            return self.isSpace
        else:
            return self.links[ascii_letters.index(char)]
    
    def setEnd(self,times: int) -> None:
        self.wordEnd+= times
    
    def wordEndCount(self) -> int:
        return self.wordEnd 
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self,word: str,times: int)  -> None:
        node = self.root
        
        for char in word:
            
            if char == ' ' and not node.isSpaceExist():
                node.createSpace(TrieNode())
            elif char != ' ' and not node.containsKey(char):
                node.insertKey(char,TrieNode())    
            
            node = node.getRefNode(char)           
            
        node.setEnd(times)
    
    def getSuggestions(self,prefix,curr,ans):
        
        wordEnd = curr.wordEndCount()
        
        if wordEnd:
            if wordEnd not in ans:
                ans[wordEnd] = []
            ans[wordEnd].append(prefix)

        for char in ascii_lowercase:
            if curr.containsKey(char):
                temp = prefix
                prefix+=char
                self.getSuggestions(prefix,curr.getRefNode(char),ans)
                prefix = temp
        
        if curr.isSpaceExist():
            temp = prefix
            prefix+=' '
            self.getSuggestions(prefix,curr.getRefNode(' '),ans)
            prefix = temp

class AutocompleteSystem:
    def __init__(self,searches: List[str],times: List[int]) -> None:
        
        self.prefix = ''
        self.trie = Trie()
        self.prev = self.trie.root
        self.stop = False

        for i in range(len(searches)):
            self.trie.insert(searches[i],times[i])
            
    def format(self,ans):
        ans = list(ans.items())
        ans.sort(reverse=True)
        newAns = []
        
        for count,words in ans:
            if len(newAns) == 3:
                break
            words.sort()
            newAns.extend(words)
        
        while len(newAns) > 3:
            newAns.pop()
        
        return newAns 

    def input(self, c: chr) -> List[str]:

        if self.stop:
            return []
        
        ans = {}
        
        if c == '#':
            self.prefix = ''
            return []
        
        if c != ' ' and not self.prev.containsKey(c):
            self.stop = True
            return []

        if c == ' ' and not self.prev.isSpaceExist():
            return []

        self.prefix+=c
        
        self.prev = self.prev.getRefNode(c)
        
        self.trie.getSuggestions(self.prefix,self.prev,ans)
        
        return self.format(ans)