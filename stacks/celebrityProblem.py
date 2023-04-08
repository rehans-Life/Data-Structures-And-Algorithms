# Brute Force

# Time Complexity: O(n^2)
# Space Complexity: O(1)

matrix = [
    [0,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,1,1,0]
]

def celebrityProblem(matrix):
    
    n = len(matrix)
    
    for i in range(n):
        
        if sum(matrix[i]) == 0:
            peopleKnowI = 0
            
            for j in range(n):
                if matrix[j][i] == 1:
                    peopleKnowI+=1
            
            if peopleKnowI == n-1:
                return True
    
    return False


# print(celebrityProblem(matrix))


def knows(A,B,matrix):
    
    # If in person's A row in the B column we see a 1 then we know A knows him so we return True or else False
    if matrix[A][B] == 1:
        return True
    else:
        return False
        

def celebrityProblemI(matrix,n):
    
    stack = list()
    
    # Adding all the persons into the stack
    for i in range(n):
        stack.append(i)
        
    # Running a while loop that runs until our stack has only one person inside of it.
    while len(stack) > 1:
        
        # We take a two persons out
        
        A = stack.pop()
        B = stack.pop()
        
        # If person A knows B then it cannot be our celebrity because we know a celebrity doesnt know anyone
        # But B can still be our celebrity because A knows him and the remaining persons could also endup knowing him.
        # So we bring him back
        if knows(A,B,matrix):
            stack.append(B)
        else:
        # If person A doesnt know B then B fosure not our celeberity cause then everybody doesnt know him since A doesnt 
        # hum but A can be our cause he doesnt B and can still endup knowing no one so we bring him back.
            stack.append(A)
            
    # The final person in our stack can be our possible celebrity.
    ans = stack.pop()
    
    # Confirming it is our answer by checking its row and column
    
    # If candidate doesnt know anyone then its row sum would be zero and if he does then there would be a one and it
    # wouldnt be our answer then.
    rowCheck = True if sum(matrix[ans]) == 0 else False   
    
    colCheck = False
    colCount = 0
    
    for i in range(n):
        if matrix[i][ans] == 1:
            colCount+=1
        colCheck = True if colCount == n-1 else False
        
    if rowCheck and colCheck:
        return ans
    else:
        return -1
    
    
print(celebrityProblemI(matrix,len(matrix)))
    
        

    
    
    
    
    
    
    
    