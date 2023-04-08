from typing import List
from collections import deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            
            # The length of the window is going to be equal to that of the word p 
            
            # Because of the length of an anagram of a word is equal to that of the word.

            # So i need to check each continious part of length equal to the word inside of the array
            # And check if it is an anagram or not. because if an agagram exists then its going to be 
            # exactly of that length 
            k = len(p)

            # Maitaining a hash table to count the frequencies of the each element inside of the word
            # whose anagrams im searching for in the array
            freq = dict()

            for char in p:
                if char not in freq:
                    freq[char] = 0
                freq[char]+=1
            
            # Count variable which is going to store how many more elements are required to be striked
            # out by the window for it to be an anagram
            count = len(freq)

            # I will be checking each window of size and check if it is an anagram or not
            i,j=0,0

            # An array which is going to store the starting index of each anagram inside of the array
            ans = []

            while j < len(s):
                # The calculation for the sliding window here is that if j pointer is pointing at an
                # character in the string which is in the map i decrement that character

                # If that characters frequency goes to zero then that means the frequncy of that character
                # in the window is equal to its frequency in the actual word itself 

                # Hence in that case i can strike an element out by decrementing the count 

                if s[j] in freq:
                    freq[s[j]]-=1
                    if freq[s[j]] == 0:
                        count-=1

                # I keep moving my j pointer until my windows size hits K
                if (j-i+1) < k:
                    j+=1
                elif (j-i+1) == k:
                    # Now i use my calculations I've made to check if my current window is an anagram or not
                    
                    # So basically if my count is zero that means my current window consists of all the letters
                    # of the given word and also the frequency of each of those letters in equal to that of the 
                    # word hence my current window is an anagram

                    # However if count is not zero then that means there are some letters which are either not 
                    # present in the current window of the actual word or the frequency of some letters of the
                    # word is not equal to that of the window either of these make my current window not 
                    # an anagram of my word.

                    if count == 0:
                        ans.append(i)

                    # Sliding the Window.
                    
                    # Here before i slide to my new window i need to check if my current ith element is present
                    # in the hashmap or not 

                    # Becuase i need to undo the changes i've made in relation to the ith character because its
                    # not going to be present inside of the new window 

                    # And undoing the changes means incrementing that element because i wouldve decremented it
                    # it previously.

                    # Now also if this character was previously zero then i need to increment my count also
                    # its because it means that this elements frequency in the window is not equivalent to
                    # that of its frequency in the actual word so i would unstrike that element since it was 
                    # previously striked off So I need to increment my count to unstrike it.

                    if s[i] in freq:
                        freq[s[i]]+=1
                        if freq[s[i]] == 1:
                            count+=1
                    
                    j+=1
                    i+=1 

            return ans

