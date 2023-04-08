class NStack:
    def __init__(self, n, s):
        # Initializing our array of size s which is going to contain our n
        # stacks.
        self.stack = [0] * s

        # Initizling our top array of size equivalent to number of stacks to be
        # implemented and its going to store indexes of top elements of each
        # stack.
        self.top = [-1] * n

        # Our next arr where if index is empty in the array then it points
        # towards the next empty space in the array or else if its not empty
        # then it points at the prev top of the stack of it is a part of
        self.next = [i+1 for i in range(s)]
        self.next[s-1] = -1
        # Our freespot index pointer which points at the empty index in the
        # array.
        self.freespot = 0

        self.size = s

    def push(self, x, m):
        # Checking if there is space in the array cause only then we can
        # insert more elements into the array.

        if self.freespot > -1:

            # Storing the freespot index inside of the array.
            index = self.freespot

            # Updating the freespot pointer to the next free index in the
            # array
            self.freespot = self.next[index]

            # Placing the val at the freespot
            self.stack[index] = x

            # Then we know this element is now the new top of the current
            # mth stack.

            # So its next arr value should now point towards the prev top
            # and it should become the new top

            self.next[index] = self.top[m-1]

            self.top[m-1] = index

            return True

        else:
            return False

    def pop(self, m):
        # So we will check if the stack in which we trying pop elements out of
        # does it actually contain some elements
        if self.top[m-1] == -1:
            return -1

        index = self.top[m-1]

        # Updating the top of the stack to the prev top index which we can
        # access through the value of index which we are removing in next arr
        self.top[m-1] = self.next[index]

        # So we need to make this index point towards the next freespot
        # and make this the current freespot
        self.next[index] = self.freespot

        self.freespot = index

        return self.stack[index]
