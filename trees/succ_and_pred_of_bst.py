"""
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
"""


def predecessorSuccessor(root, key):
    predecessor = -1
    successor = float('inf')

    # FInding successor
    curr = root
    while curr:
        if curr.data <= key:
            curr = curr.right
        else:
            if curr.data < successor:
                successor = curr.data
            curr = curr.left

    # Finding predecessor
    curr = root
    while curr:
        if curr.data < key:
            if curr.data > predecessor:
                predecessor = curr.data
            curr = curr.right
        else:
            curr = curr.left

    if successor == float('inf'):
        successor = -1
    return predecessor, successor