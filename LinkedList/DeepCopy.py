# Definition for singly-linked list with a random pointer.

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        new_head = RandomListNode(head.label)

        curr = head
        new_curr = new_head
        rand_map = dict()
        rand_map[curr] = new_curr

        while curr and (curr.next or curr.random):
            if curr.next and curr.next in rand_map:
                new_curr.next = rand_map[curr.next]
            elif curr.next:
                new_next = RandomListNode(curr.next.label)
                rand_map[curr.next] = new_next
                new_curr.next = new_next

            if curr.random and curr.random in rand_map:
                new_curr.random = rand_map[curr.random]
            elif curr.random:
                new_random = RandomListNode(curr.random.label)
                rand_map[curr.random] = new_random
                new_curr.random = new_random

            curr = curr.next
            new_curr = new_curr.next
        return new_head