# https://www.lintcode.com/problem/serialize-and-deserialize-binary-tree/description?_from=ladder&&fromId=1
#Definition of TreeNode:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if not root:
            return []

        node = root
        q = [node]
        series = []
        while q:
            layer_size = len(q)
            next_layer = []
            for _ in range(layer_size):
                curr_node = q.pop(0)
                if not curr_node:
                    next_layer.extend([False, False])
                    series.append('#')
                else:
                    series.append(curr_node.val)
                    if curr_node.left:
                        next_layer.append(curr_node.left)
                    else:
                        next_layer.append(False)
                    if curr_node.right:
                        next_layer.append(curr_node.right)
                    else:
                        next_layer.append(False)
            if any(next_layer):
                q += next_layer

        return series

    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        m = len(data)
        nodes = [TreeNode(x) if x != '#' else None for x in data]

        for i in range(m):
            if nodes[i]:
                if i * 2 < m:
                    nodes[i].left = nodes[2 * i]
                if i * 2 + 1 < m:
                    nodes[i].right = nodes[2 * i + 1]
        return nodes[0]


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node2.right = node3

s = Solution()
print(s.serialize(node1))
print(s.deserialize(s.serialize(node1)))