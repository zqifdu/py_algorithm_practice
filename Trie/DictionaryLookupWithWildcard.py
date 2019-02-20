"""
Given a list of words in dictionary, search if a quest word is in that dictionary.
'.' in a word means it can match any character.
"""


# # Trie node
# class node:
#     def __init__(self, char, is_end=True):
#         self.char = char
#         self.children = {}
#         self.is_end = is_end
#
# # Build a tree
# class trie(object):
#     def __init__(self):
#         self.root = node('', )
#
#     def setup(self, list_of_word):
#         for word in list_of_word:
#             self._add_to_trie(word)
#
#     def _add_to_trie(self, word):
#         curr = self.root
#         for c in word:
#             if c in curr.children:
#                 c =
#                 continue
#             else:

class Node:
    def __init__(self, char, is_end=False):
        self.char = char
        self.children = dict()
        self.is_end = is_end


class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = Node('')

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        # write your code here
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Node(c)
                curr = curr.children[c]
        curr.is_end = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        # write your code here
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.is_end

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        # write your code here
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True


