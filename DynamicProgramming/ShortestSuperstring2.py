"""
https://leetcode.com/problems/find-the-shortest-superstring/
"""


class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)

        # overlaps between any two words in the list A
        # overlap[i][j]: overlap length when put word j behind word i
        overlap = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    for len_overlap in range(min(len(A[i]), len(A[j])), -1, -1):
                        if A[i].endswith(A[j][:len_overlap]):
                            overlap[i][j] = len_overlap
                            break

        # Dynamic programming to find the optimal overlap
        dp = [[0] * N for _ in range(1 << N)]
        trace = [[None] * N for _ in range(1 << N)]

        # mask iterates through all possible subsets
        for mask in range(1, 1 << N):
            for j in range(N):
                # if jth node has been visited
                if (mask >> j) & 1:
                    # if j has been visited; delete j
                    pmask = mask ^ (1 << j)
                    if pmask == 0:
                        continue
                    for i in range(N):

                        # if ith node has been visited
                        if (pmask >> i) & 1:

                            overlap_end_ij = dp[pmask][i] + overlap[i][j]

                            if overlap_end_ij >= dp[mask][j]:
                                dp[mask][j] = overlap_end_ij
                                trace[mask][j] = i

        # Find the final word that was put into the superstring
        max_overlap_ind = max(range(N), key=dp[-1].__getitem__)
        word_ind = []
        last_ind = max_overlap_ind
        mask = (1 << N) - 1
        while last_ind is not None:
            word_ind.append(last_ind)
            mask, last_ind = mask ^ (1 << last_ind), trace[mask][last_ind]

        word_ind = word_ind[::-1]
        seen = [False] * N
        for i in word_ind:
            seen[i] = True
        word_ind.extend([i for i in range(N) if not seen[i]])

        ans = [A[word_ind[0]]]
        for i in range(1, N):
            noverlap = overlap[word_ind[i - 1]][word_ind[i]]
            ans.append(A[word_ind[i]][noverlap:])

        return "".join(ans)


if __name__ == '__main__':
    s = Solution()

    strs = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]

    print(s.shortestSuperstring(strs))