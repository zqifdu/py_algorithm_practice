"""
Given root node and two arbitrary nodes (node1 and node2), find the lowest common ancestor of this two nodes
"""

class node():
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class solution:
    def findLCAwRoot(root, node1, node2):
        # deivide and conquer
        if not root.left and not root.right:
            return None

        # root is one of the node
        if root == node1:
            return node1
        if root == node2:
            return node2
        if not root.left and root != node1 and root != node2:
            return self.findLCAwRoot(root.right)
        elif not root.right and root != node1 and root != node2:
            return self.findLCAwRoot(root.left)
        elif root.left and root.right:
            left_LCA = self.findLCAwRoot(root.left, node1, node2)
            right_LCA = self.findLCAwRoot(root.right, node1, node2)
            # LCA is in the left part or right part
            if left_LCA is None or right_LCA is None:
                return left_LCA if left_LCA else right_LCA
            # Left/right part has found only one node
            elif (left_LCA == node1 and right_LCA == node2) or (left_LCA == node2 and right_LCA == node1):
                return root

    def findLCAwoRoot(self, node1, node2):
        # hashmap
        node1_anc = {node1}
        while node1.parent:
            node1 = node1.parent
            node1_anc.add(node1)

        if node2 in node1_anc:
            return node2
        while node2.parent:
            node2 = node2.parent
            if node2 in node1_anc:
                return node2


    # Emmm, this is not constant space because recursion is used
    def findLCAwoRoot2(self, node1, node2):
        if node1.left and self.nodeInTree(node1.left, node2):
            return node1
        if node1.right and self.nodeInTree(node1.right, node2):
            return node1
        while node1.parent:
            if node1.parent == node2:
                return node2
            if node1 == node1.parent.left:
                if self.nodeInTree(node.parent.right, node2):
                    return node1.parent
            elif node1 == node1.parent.right:
                if self.nodeInTree(node.parent.left, node2):
                    return node1.parent
            node1 = node1.parent


    def nodeInTree(self, root, node):
        if root == node:
            return True

        in_left, in_right = False, False
        if root.left:
            in_left = self.nodeInTree(root.left, node)
        if root.right:
            in_right = self.nodeInTree(root.right, node)
        return in_left or in_right