"""
https://leetcode.com/problems/cracking-the-safe/
"""


# Find Eular path
# Hierholzer algorithm: postorder dfs
def crackSafe(k, n):
    ans = []
    visited = set()
    def dfs(curr):
        for i in range(k):
            if curr + str(i) not in visited:
                new_curr = curr + str(i)
                visited.add(new_curr)
                dfs(new_curr[1:])
                ans.append(str(i))

    dfs('0' * (n-1))

    return "".join(ans) + "0" * (n-1)


# Find Hamilton path
def crackSafe2(k, n):

    visited = set()
    visited.add('0'*n)

    path = []

    def dfs(node, path):
        if len(visited) == k**n:
            return True
        for i in map(str, range(k)):
            if node[1:] + i not in visited:
                visited.add(node[1:] + i)
                path.append(i)
                if dfs(node[1:] + i, path):
                    return True
                visited.remove(node[1:] + i)
                path.pop()

    path = ['0'] * (n - 1)
    dfs('0' * n, path)
    path.append('0')
    return "".join(path)


if __name__ == '__main__':
    print(crackSafe(3, 3))
    print(crackSafe2(3, 3))
