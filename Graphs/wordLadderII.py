from queue import Queue
from string import ascii_lowercase

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        
        # An array to store all of my shortest sequences 
        ans = []
        
        # A queue to store our sequences that we generate upon each 
        # iteration
        queue = Queue()
        
        # Initally our queue will have the sequence with only the start
        # word cause thats from where our sequence starts off with
        queue.put([startWord])
        
        # Then we need the word list in set form so that we can efficently
        # search and delete items out of it after the word has been used
        # by the sequences of the same length
        words = set(wordList)
        if startWord in words: words.remove(startWord)
        endBfs = False
        
        while not queue.empty() and not endBfs:
            # Then we need to make sure we traverse all the seuquences
            # of the same length in one go and find there consecutive 
            # sequences so we can allow all of them to have access to 
            # the same words
            
            # We need to store the words they have used and then delete
            # them after they have generated their consecutive sequences
            wordsUsed = set()
            
            # Getting the queue size so we only take out sequences of same 
            # length
            qSize = queue.qsize()
            
            for _ in range(qSize):
                sequence = queue.get()
                n = len(sequence)
                
                # Getting the last word out cause thats from where i will
                # find the next word within the sequence
                word = sequence[n-1]
                m = len(word)
                
                # If one of the sequences on the level has reached 
                # the target word then i can append it to my answer
                # And in order to stop the traversel after this level
                # i set a varaible true also i dont want to generate
                # anymore sequences from this seuqence i continue and 
                # move to the next sequence.
                if word == targetWord:
                    ans.append(sequence)
                    endBfs = True
                    continue
                
                # Since we need all the possible words that could after
                # this in the sequence so we need to replace its each
                # character with all 26 alphabets and check which of 
                # them lies within the wordList and if someone does then
                # thats of the possible words that could exist after in
                # the sequence and we insert that new sequence into the
                # queue.
                for i in range(m):
                    
                    # Each character we gon replace with all 26 alphabets
                    for alphabet in ascii_lowercase:
                        # Replacing the alphabet with the character in
                        # the word.
                        newWord = word[0:i] + alphabet + word[i+1:m]
                        # If this new word exists hence this is a possible
                        # word that would exists next in the sequence
                        # So we insert the new sequence into the queue
                        # along with the new word in it
                        if newWord in words:
                            # We also insert the word in our used words
                            # set so we can delete it from the word list
                            # later on.
                            wordsUsed.add(newWord)
                            # We also create a new sequence which is 
                            # a copy of the current sequence but with
                            # the new word of the sequence inside of it
                            newSequence = sequence.copy()
                            newSequence.append(newWord)
                            # Then we insert that sequence into our
                            # queue to find the target word through it.
                            queue.put(newSequence)
            
            # Deleting the words i used in this iteration from the word
            # list
            for usedWord in wordsUsed:
                words.remove(usedWord)
        
        return ans
                    