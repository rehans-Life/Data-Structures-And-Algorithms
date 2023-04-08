from queue import Queue
from string import *

# This approach follows a dfs traversl to generate all the shortest
# sequences but we are going to generate them in a reverse order
# So basically im going to start from the target word and then go
# backwards and generate the shortest sequences to the start word

# But how will this be more efficient and how will we apply dfs
# if we dont know whats the shortest sequence.

# Actually what we are going to do first is perform a word ladder I and 
# hence find all the words that can exists upto the first shortest
# sequence and we are also going to find their positions as well 
# and map the words to their positions within the shortest sequence
# using a hashmap.

# Then we start a dfs in reverse from the target word itself and try
# to go backwards and find the all the shortest sequences from the
# target word to the start word therefore i can just reverse all of 
# them and get my shortest sequences from start to target word.

# And we are going to do it is we are going to find all the words that
# can exists behind it in the sequence using the brute force technique
# of replacing each character by all 26 alphabets.

# But the words that can exists behind arent going to found using the
# wordlist 

# But this time we are going to check within our map which stores
# the words we have generated upto the shortest sequence and we will check
# does it exists inside of there and also is it actually behind our
# target word in the shortest sequence cause we have mapped all the 
# words to there positions in the map if it does then we add it
# to the sequence and recursively follow this procedure to generate
# the sequence till the start word

# We also apply backtracking so that we can move onto the generating 
# all the shortest sequences 

# And why is this more efficient right so since we are going in backwards
# direction and we already know word exists behind each word in the 
# sequence hence here we will avoid checking all the sequences like
# we do in bfs and when we start from starting word we will always 
# be generating those sequences which are the shortest.

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
    
    # Step 1:    
        
        # First generate words till the first shortest sequence
        # and find there positions and map the words to them
        # for this apply the word ladder I approach
        
        # A queue to store the words within the sequence
        queue = Queue()
        
        # A hashmap to map all the words to their positions within
        # the shortest sequences
        shortSequence = dict()
        
        # Initially we include our start word within queue cause
        # thats where our sequence will start of from.
        
        # And we know the start words position will always be zero
        # within the shortest sequence
        queue.put(startWord)
        shortSequence[startWord] = 0 
        
        # A set storing our word list so we can efficient delete words
        # from it as we insert items into our sequence
        words = set(wordList)
        
        # If starting word exists we remove cause its already used
        if startWord in words: words.remove(startWord)
        
        while not queue.empty():
            # Getting the last word within the current sequence
            # cause thats from where we will get the next word of
            # sequence from
            word = queue.get()
            m = len(word)
            # Using the brute force technique to generate all possible
            # words that can exists after this word
            for i in range(m):
                for alphabet in ascii_lowercase:
                    # Using list slicing to replace the ith character
                    # to replace it all the alphabets one by one
                    newWord = word[0:i] + alphabet + word[i+1:m]
                    
                    # If it exists in word list hence its a word next
                    # in the sequence
                    if newWord in words:
                        # We add it in the queue we map it to its
                        # position and also remove it from the wordlist
                        # so it cant be inserted again into some other
                        # sequence
                        queue.put(newWord)
                        # Its going to be one position ahead of the 
                        # current word
                        shortSequence[newWord] = shortSequence[word] + 1
                        # Removing from the word list
                        words.remove(newWord)
            
        # After this our map has mapped each word to its position which
        # exists within the shortest sequences.
        
        # Now we perform a dfs and generate all the possible 
        # shortest seqeuences from end to start Word.
        
        # A squence array from we generte the sequences and we also
        # backtrack on this array
        sequence = []
        
        # Initially our sequence will start from the target word
        sequence.append(targetWord)
        
        # An array to store our shortest sequences
        ans = []
        
        # Our dfs function
        def dfs(word: str):
            
            # If current word is in our startword hence we got our
            # shotest sequence so we can append a copy of it in our
            # answer and also reverse it so get the sequence from 
            # start to end
            if word == startWord:
                sequenceCopy = sequence.copy()
                sequenceCopy.reverse()
                ans.append(sequenceCopy)
            
            m = len(word)
            
            # Then we generate all possible words before this in our
            # sequence for that it should exist within our position
            # map which is storing the words till the shortest sequence
            # And it should be directly behind our current word in 
            # the shortest sequence for that we check the positios
            for i in range(m):
                for alphabet in ascii_lowercase:
                    # Checking if new word is actually the word behind it
                    newWord = word[0:i] + alphabet + word[i+1:m]
                    
                    if newWord in shortSequence and shortSequence[word] - shortSequence[newWord] == 1:
                        # If it is behind this word then we include them 
                        # in our sequence and recrusively generate 
                        # the shortest sequence from it
                        sequence.append(newWord)
                        dfs(newWord)
                        # After we have returned we backtrack
                        # by removing word and check to see if there is
                        # another word from where there exists a
                        # sequence.
                        sequence.pop()
                    
        # Generating all shortest sequences from endWord to start using dfs. 
        dfs(targetWord)
        # Then returning all shortest sequences we generated.
        return ans
    
