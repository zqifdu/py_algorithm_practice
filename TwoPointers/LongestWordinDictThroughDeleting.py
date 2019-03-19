"""
LeetCode 524
"""

# DFS + Trie (Time limit exceeded)
class Node(object):
    def __init__(self, c, is_end):
        self.c = c
        self.is_end = is_end
        self.children = dict()


class Trie(object):
    def __init__(self):
        self.root = Node('', False)

    def add(self, word):
        curr = self.root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Node(c, i == len(word) - 1)
                curr = curr.children[c]


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not s:
            return ""

        trie = Trie()
        for w in d:
            trie.add(w)

        candidates = []
        curr = ''

        self.dfs(s, 0, trie.root, candidates, curr)
        candidates.sort()
        candidates.sort(key=len, reverse=True)

        if candidates:
            return candidates[0]
        return ''

    def dfs(self, s, i, root, candidates, curr):
        if not root:
            return

        if root.is_end:
            candidates.append(curr)

        if i == len(s) - 1:
            if s[i] in root.children and root.children[s[i]].is_end:
                curr += s[i]
                candidates.append(curr)
            return

        if s[i] in root.children:
            self.dfs(s, i + 1, root.children[s[i]], candidates, curr + s[i])

        self.dfs(s, i + 1, root, candidates, curr)



# Sort and compare one by one

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        d.sort(key=len, reverse=True)

        for w in d:
            i_w, i_s = 0, 0
            ans = ''
            while i_w < len(w) and i_s < len(s):
                if s[i_s] == w[i_w]:
                    ans += s[i_s]
                    i_s += 1
                    i_w += 1
                    continue
                i_s += 1
            if i_w == len(w):
                return ans
        return ''

