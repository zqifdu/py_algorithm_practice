"""
Given a list of daily temperature A, return a list such that, for each day in A,
tells you how many days you would have to wait until a warmer temperature. If there is
no future day for which this is possible, put 0 instead.
"""


# Using a monotonically decreasing stack

def next_hotter_day(temps):
    # Store the indices an monotonically decreasing array in the temps list
    # ending with the current temp
    dec_stack = []
    ans = [0] * len(temps)
    
    for i, temp in enumerate(temps):

        while dec_stack and temp > temps[dec_stack[-1]]:
            pre_index = dec_stack.pop()
            ans[pre_index] = i - pre_index

        dec_stack.append(i)

    return ans


print(next_hotter_day([73, 74, 75, 71, 69, 72, 76, 73]))