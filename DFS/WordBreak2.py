"""
https://www.lintcode.com/problem/word-break-ii/
"""


# My solution version 1
class trie_node:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word = ""


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        word_trie_root = self.build_trie(wordDict)
        ans = []
        # answer of subproblem (starting from index i)
        ind_ans = dict()
        # words starting from index i
        ind_word_dict = dict()
        self.dfs(s, word_trie_root, 0, ans, [], ind_word_dict, ind_ans)

        return ans

    def dfs(self, s, word_trie_root, start, ans, words, ind_word_dict, ind_ans):
        if start == len(s):
            print(words)
            ans.append(" ".join(words))
            return

        if start in ind_word_dict:
            next_words = ind_word_dict[start]
        else:
            # Search through the word_trie
            next_words = []
            curr_node = word_trie_root
            for char_ind in range(start, len(s)):
                char = s[char_ind]
                found_in_child = False
                for child in curr_node.children:
                    if char == child.char:
                        found_in_child = True
                        if child.word != "":
                            next_words.append(child.word)
                        curr_node = child
                        break
                if not found_in_child:
                    break
            ind_word_dict[start] = next_words
            print(start, ind_word_dict[start])

        if not next_words:
            return

        ans_from_start = []
        for next_word in next_words:
            if start + len(next_word) in ind_ans:
                ans_from_start += [[next_word] + words for words in ind_ans[start + len(next_word)]]
            else:
                self.dfs(s, word_trie_root, start + len(next_word), ans, words + [next_word],
                         ind_word_dict, ind_ans)

        ind_ans[start] = ans_from_start


    def build_trie(self, wordDict):
        root = trie_node("")

        for word in wordDict:
            curr_node = root
            for char in word:
                char_node_exist = False
                for child in curr_node.children:
                    if char == child.char:
                        char_node_exist = True
                        curr_node = child
                        break
                if not char_node_exist:
                    new_node = trie_node(char)
                    curr_node.children.append(new_node)
                    curr_node = new_node

            curr_node.word = word
        return root

# test cases
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

sol = Solution()
print(sol.wordBreak(s, wordDict))

# Ling Huchong's solution
class Solution2:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    # 找到 s 的所有切割方案并 return
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)

        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions
        print(s, memo[s])
        return partitions

# test cases
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

sol = Solution2()
print(sol.wordBreak(s, wordDict))
