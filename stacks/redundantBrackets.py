def findRedundantBrackets(s: str):

    stack = list()

    for i in range(len(s)):

        char = s[i]

        if char in '(*/-+':
            stack.append(char)
        else:
            if char == ')':
                if stack[len(stack)-1] == '(':
                    return 'Yes'
                else:
                    while stack[len(stack)-1] in '+/-*':
                        stack.pop()

                    stack.pop()

    return 'No'

print(findRedundantBrackets('((a*b)*(c+b))*((d)+b)'))