class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeRunner:
    def __init__(self):
        pass

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)

    def height(self, node):
        if node is None:
            return 0
        lheight = self.height(node.left)
        rheight = self.height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def max_path_to_leaf(self, node, sumpath):
        if node is None:
            # print('reached leaf with path %s' % sumpath)
            return sumpath
        nodesum = node.val + sumpath
        return max(
            self.max_path_to_leaf(node.left, nodesum),
            self.max_path_to_leaf(node.right, nodesum))

    def totalsum(self, node):
        if node is None:
            return 0
        return node.val + self.totalsum(node.left) + self.totalsum(node.right)

    def paths_to_leaf(self, node, path):
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None:
            print(path)
            path.remove(node.val)
            return
        self.paths_to_leaf(node.left, path)
        self.paths_to_leaf(node.right, path)

    def bfs(self, root):
        from collections import deque
        queue = deque()
        queue.appendleft(root)
        while queue:
            node =  queue.pop()
            if node is None:
                continue
            print(node.val)
            queue.appendleft(node.left)
            queue.appendleft(node.right)


def main():
    # construct tree
    tn1 = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    tn4 = TreeNode(4)
    tn5 = TreeNode(5)
    tn6 = TreeNode(6)
    tn7 = TreeNode(7)

    tn2.left = tn4
    tn2.right = tn5
    tn3.left = tn6
    tn3.right = tn7

    tnleg1 = TreeNode(58)
    tnleg2 = TreeNode(74)
    tnleg1.right = tnleg2
    # tn2.left = tnleg1
    tn1.left = tn2
    tn1.right = tn3

    # run traversals
    import tr_nonrecurse
    trn = tr_nonrecurse.TreeNonRecursive()
    tn1pre = tn1
    tn1post = tn1
    prenonr = trn.pre_nonrecursive(tn1pre)
    postnonr = trn.post_nonrecursive(tn1post)
    print('pre non-recurse: %s' % prenonr)
    print('post nonr: %s' % postnonr)
    tr = TreeRunner()
    print('BFS')
    tr.bfs(tn1)
    print('in order')
    tr.inorder(tn1)
    print('pre order')
    tr.preorder(tn1)
    print('post order')
    tr.postorder(tn1)
    max = tr.max_path_to_leaf(tn1, 0)
    print('max %s' % max)
    height = tr.height(tn1)
    print('Height %s' % height)
    # sum = tr.totalsum(tn1)
    # print(sum)
    # tr.paths_to_leaf(tn1, path=[])


if __name__ == "__main__":
    main()