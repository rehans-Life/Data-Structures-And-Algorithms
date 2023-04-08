def floorInBST(root, X):
    ans = -1

    while root:
        if root.data == X:
            return root.data
        elif root.data < X:
            ans = root.data
            root = root.right
        else:
            root = root.left

    return ans