"""
Description

Given a list of numbers (without duplicates) and a target number, find all unique combinations using the list of numbers that sum to the target

Note: The same number in your list of numbers can be used more than once
"""


# My solution 1
def sumToTarget2(num_list, target):
    ans = []
    sol = []
    num_list.sort()
    dfs2(num_list, target, 0, ans, sol, [False]*len(num_list))

    return ans


def dfs2(num_list, target, start_ind, ans, sol, visited):
    if target == 0:
        ans.append(list(sol))
        return
    if target < 0:
        return

    for i in range(start_ind, len(num_list)):
        # Avoid duplicates
        if i - 1 >= 0 and (not visited[i-1]) and num_list[i] == num_list[i-1]:
            continue
        # Backtracking
        sol.append(num_list[i])
        visited[i] = True
        dfs2(num_list, target - num_list[i], i + 1, ans, sol, visited)
        visited[i] = False
        sol.pop()
    return


num_list = [10,1,2,7,6,1,5]
target = 8
print(sumToTarget2(num_list, target))

num_list = [2,5,2,1,2]
target = 5
print(sumToTarget2(num_list, target))


# My solution 2
def sumToTarget(num_list, target):
    ans = []
    sol = []
    dfs(num_list, target, 0, ans, sol)
    return ans


def dfs(num_list, target, start_ind, ans, sol):
    if target == 0:
        ans.append(list(sol))
        return
    if target < 0:
        return

    for i in range(start_ind, len(num_list)):
        sol.append(num_list[i])
        dfs(num_list, target - num_list[i], i, ans, sol)
        sol.pop()

    return


num_list = [2, 3, 5]
target = 7
print(sumToTarget(num_list, target))
num_list = [2, 3, 5]
target = 8
print(sumToTarget(num_list, target))