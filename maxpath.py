# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, tree):
        maxp = 0
        path = []
        maxp = self.traverseAllPathsToLeaf(tree, path, maxp)
        return maxp

    def traverseAllPathsToLeaf(self, tree, path, total):
        if tree is None:
            return

        # Add this tree node to the path, augment total
        path.append(tree.val)
        total += tree.val

        if tree.left is None and tree.right is None:
            # print the path and sum to get here
            print('Path to leaf %s with sum %s' % (path, total))

        self.traverseAllPathsToLeaf(tree.left, path, total)
        self.traverseAllPathsToLeaf(tree.right, path, total)


    def traverseTree(self, tree):
        if tree.left is None and tree.right is None:
            print('At the end of a leaf with value %s' % tree.val)
            return
        print('Traverse tree with value %s' % tree.val)
        for subtree in [tree.left, tree.right]:
            self.traverseTree(subtree)

    def traverseTreeMaxPath(self, tree, maxp):
        # maxp is the maximum path from the root to this node
        if tree.left is None and tree.right is None:
            print('At the end of a leaf with value %s, maxpath %s' % (tree.val, maxp))
            return maxp + tree.val
        print('Traverse tree with value %s' % tree.val)
        for subtree in [tree.left, tree.right]:
            maxp += self.traverseTreeMaxPath(subtree, maxp)
        return maxp + tree.val


def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    sol = Solution()
    print(sol.maxPathSum(tree))
main()