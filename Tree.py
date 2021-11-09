# Class node implementation
class Node:
    def __init__(self, currentnode, previousnode, g, h, dir):
        self.currentnode = currentnode
        self.previousnode = previousnode
        self.g = g
        self.h = h
        self.dir = dir

    def f(self):
        return self.g+self.h


# Insertion function in BST
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
