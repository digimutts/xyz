import stackll
import queuell
class TreeNonRecursive:
    """
    Non-recursive tree methods
    """
    def __init__(self):
        pass

    def pre_nonrecursive(self, node):
        # go to each leaf, put vals on a stack
        stack = stackll.StackLL()
        stack.push(node)
        pre = []
        while not stack.is_empty():
            node = stack.pop()
            if node is None:
                continue
            pre.append(node.val)
            # go all the way to right, then left
            # (stack will return these in reverse)
            stack.push(node.right)
            stack.push(node.left)
        return pre

    def post_nonrecursive(self, node):
        stack = stackll.StackLL()
        stack.push(node)
        post = []
        while not stack.is_empty():
            node = stack.pop()
            if node is None:
                continue
            # go all the way to right, then left
            # (stack will return these in reverse)
            stack.push(node.right)
            stack.push(node.left)

            post.append(node.val)
        return post







