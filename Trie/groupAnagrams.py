from collections import defaultdict
from string import ascii_letters,ascii_lowercase
from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.flag = False
        self.anagrams = []
    
    def containsKey(self,char: int) -> bool:
        return self.links[ascii_letters.index(char)]
    
    def insertKey(self,char: str,trieNode: 'TrieNode') -> None:
        self.links[ascii_letters.index(char)] = trieNode
    
    def getRefNode(self,char: str) -> 'TrieNode':
        return self.links[ascii_letters.index(char)]

    def setEnd(self) -> None:
        self.flag = True

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word: str) -> None:
        # First Im going to sort the word then insert it into the trie so that 
        # words which are anagrams of each other would overlap each other in the trie.
        sortedWord = sorted(word)
        node = self.root

        for char in sortedWord:
            if not node.containsKey(char):
                node.insertKey(char,TrieNode())
            node = node.getRefNode(char)
        
        node.setEnd()
        # Appending the unsorted word in the angrams array of the last character 
        # in its sorted state 
        # Since the sorted version of two words which are anagrams of each other is same
        # hence i will store all the anagrams in one array itself.
        node.anagrams.append(word)
    
    # Im going to find all the end nodes and add the anagrams array into my res
    def searchAnagrams(self,curr,res) -> None:
        # Wherever flag is set to True hence there i have anagrams of a set of 
        # characters so i need to add them to my results array
        if curr.flag: 
            res.append(curr.anagrams)

        # Searching for characters for reference node from each characters
        for char in ascii_lowercase:
            # If i find one then i recurse on it
            if curr.containsKey(char):
                self.searchAnagrams(curr.getRefNode(char),res)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        trie = Trie()
        res = []

        for word in strs: trie.insert(word)

        trie.searchAnagrams(trie.root,res)

        return res
    
# Map And Sort

# Space Complexity: O(n)
# Time Complexity: O(n * (mlog(m) + m) => O(nm*logm)

# N is the number of words and M is the length of the string.
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:

            sortedWord = str(sorted(word))

            if sortedWord not in res:
                res[sortedWord] = []
            
            res[sortedWord].append(word)

        return res.values()
    
# Count Characters

# Space Complexity: O(a) where a is the number of anagrams
# Time Complexity: O(n * (m + 26)) => O(n * m)
# Where n is the number of words and m is the average length of the word.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # By default mapping our keys to lists
        res = defaultdict(list)

        for word in strs:
            charCount = [0] * 26

            for char in word:
                charCount[ord(char) - ord('a')]+=1

            res[str(charCount)].append(word)
        
        return res.values()

