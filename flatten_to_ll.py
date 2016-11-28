class Flattener:

    def  __init__(self):
        pass

    def flatten_preorder(self, node):
        if node.left is None:
            # Already in the correct form
            pass
        else:
            # The node does have a left branch
            tmp = node.right
            # Move the left branch to right side
            node.right = node.left
            # Go all the way down this new right branch until None
            rside = node.right
            while rside.right is not None:
                rside = rside.right
            rside.right = tmp
        if node.right is not None:
            node = node.right
        return node

