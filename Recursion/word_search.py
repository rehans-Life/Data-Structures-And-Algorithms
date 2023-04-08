board = [
    ['c', 'd', 'k', 's'],
    ['o', 'd', 's', 'a'],
    ['d', 'g', 'n', 'j'],
    ['e', 'r', 'i', 'n']
    ]

# K is going to denote the letter we are search for on the board.

# Initially since ive already found the first character which is at
# index of 0 we set initial value of k as 1 cause initially we will be
# search for the first character.

def search(board,word,n,m,i,j,k=0):

    # If i call this function for a coordinate which doesnt
    # even exist or if the character by which it is represented
    # is not equal to the chracter that im currently searching
    # for then I return false.
    if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[k]:
        return False
    
    # If k is equal to the length of the board so that means we have found
    # our word and we stop.
    if k == len(word):
        return True
    

    option1 = search(board,word,n,m,i-1,j,k+1)

    option2 = search(board,word,n,m,i+1,j,k+1)

    option3 = search(board,word,n,m,i,j+1,k+1)

    option4 = search(board,word,n,m,i,j-1,k+1)

    # So if by going into either of the directions I was able to 
    # form my given word then im going return true.
    return option1 or option2 or option3 or option4

def word_search(board,word,n,m):
    
    # Brute forcing my way by using nested loops in order to find the first character
    # of the given word.

    # Using nested loops in order to traverse through the complete 2d Array.
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == word[0]:
                if search(board,word,n,m,r,c):
                    return True
    return False

# print(word_search(board,'ninjas',len(board),len(board[0])))

board1 = [
    ['n', 'd', 'k', 's'],
    ['e', 'd', 's', 'a'],
    ['e', 't', 'n', 'e'],
    ['e', 'c', 'o', 'd']
    ]

word='neetcode'

def search_word(board,word):
    rows = len(board)
    cols = len(board[0])
    path = set()
    def dfs(i,j,k=0):

        # If our k is equal to the length of the word that means
        # that we have found our word on the board
        if k == len(word):
            return True
    
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[k] or (i,j) in path:
            return False

        # Adding the current coordinate to our path which contains
        # the coordinates in our path.
        path.add((i,j))
        option1 = dfs(i+1,j,k+1)
        option2 = dfs(i-1,j,k+1)
        option3 = dfs(i,j+1,k+1)
        option4 = dfs(i,j-1,k+1)
        # After finishing the search we actually make sure to
        # undo our changes and remove the coordinate from our
        # path cause there is no need to be there anymore.
        path.remove((i,j))
        return option1 or option2 or option3 or option4        
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(r,c):
                    return True
    return False
print(search_word(board1,word))