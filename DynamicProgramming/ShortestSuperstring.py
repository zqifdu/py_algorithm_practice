"""
https://leetcode.com/problems/find-the-shortest-superstring/
"""


class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        max_len = sum(len(x) for x in A)
        n = len(A)

        dp = [[max_len] * n for _ in range(2**n)]
        trace = [[-1] * n for _ in range(2**n)]

        extend_len_matrix = self.extend_len(A)

        print(extend_len_matrix)
        for mask in range(2**n):
            # If subset has size one
            if mask & (mask - 1) == 0:
                ind = len(bin(mask & (-mask))) - 3
                dp[mask][ind] = len(A[ind])

            # ith element as the final position
            for i in range(n):
                # if ith element not visited, continue since ith element must have been visited
                if not mask & (1 << i):
                    continue
                # Find the subproblem (subset with i not visited)
                pre_mask = mask ^ (1 << i)
                # All possible last step for previous subproblem
                for j in range(n):
                    if mask & (1 << j):
                        new_len = dp[pre_mask][j] + extend_len_matrix[j][i]
                        if new_len < dp[mask][i]:
                            dp[mask][i] = new_len
                            trace[mask][i] = j

        min_final = -1
        min_len = float('inf')
        words = []
        # Find the final word that gives the shortest superstring
        for i in range(n):
            if dp[-1][i] < min_len:
                min_final = i
                min_len = dp[-1][i]

        mask = 2**n - 1
        ind = min_final
        for i in range(n-1, -1, -1):
            words.append(ind)
            pre_ind = trace[mask][ind]
            mask = mask ^ (1 << ind)
            ind = pre_ind


        words = words[::-1]
        ans = [A[words[0]]]

        for i in range(1, len(words)):
            ans.append(A[words[i]][-extend_len_matrix[words[i-1]][words[i]]:])

        return "".join(ans)

    def extend_len(self, A):
        extend_len_matrix = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    len_j = len(A[j])
                    for extend_len in range(len_j + 1):
                        if A[i].endswith(A[j][:len_j - extend_len]):
                            extend_len_matrix[i][j] = extend_len
                            break
        return extend_len_matrix


if __name__ == '__main__':
    s = Solution()

    strs = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]

    print(s.shortestSuperstring(strs))