# You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets.
# It is guaranteed that the parentheses in s form a regular bracket sequence.
#
# Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair.
# The results string should not contain any parentheses.
# ------------
# Example
#
# For string s = “a(bc)de”, the output should be
# reverseParentheses(s) = “acbde”.
#
# Input/Output
#
# [execution time limit] 4 seconds (py)
#
# [input] string s
#
# A string consisting of English letters, punctuation marks, whitespace characters and brackets. It is guaranteed that
# parentheses form a regular bracket sequence.
#
# Constraints:
# 5 ≤ s.length ≤ 55.
#
# [output] string

#
# def inverse_in_parenthesis(string):
#     if not string:
#         return string
#     left, right = 0, len(string) - 1
#     while left < right and (string[left] != '(' or string[right] != ')'):
#         if string[left] != '(':
#             left += 1
#         if string[right] != ')':
#             right -= 1
#
#     if left == right:
#         return string
#     else:
#         string = string[:left] + reverse_inside(string[left + 1:right]) + string[right+1:]
#         return string
#
#
# def reverse_inside(substr):
#     if len(substr) <= 1:
#         return substr
#     left, right = 0, len(substr) - 1
#     while left < right and (substr[left] != '(' or substr[right] != ')'):
#         if substr[left] != '(':
#             left += 1
#         if substr[right] != ')':
#             right -= 1
#     if left == right:
#         return substr[::-1]
#     else:
#         reversed_subsub = reverse_inside(substr[left + 1:right])
#         return (substr[:left] + reversed_subsub + substr[right+1:])[::-1]


def inverse_in_parenthesis(string):
    stack = []
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i+1)
        if char == ')':
            start = stack.pop()
            string = string[:start] + string[start:i][::-1] + string[i:]
    i = 0
    while i < len(string):
        char = string[i]
        if char == '(' or char == ')':
            string = string[:i] + string[i+1:]
        else:
            i += 1

    return string

#
# def inverse_in_parenthesis(string):
#     final = []
#     i = 0
#     while i < len(string):
#         if string[i] == "(":
#             temp = []
#             count = 1
#             i += 1
#             while string[i] != ")" or count == 1:
#                 if string[i] == ")" and count == 1:
#                     break
#                 elif string[i] == "(":
#                     count += 1
#                 elif string[i] == ")":
#                     count -= 1
#                 else:
#                     temp.append(string[i])
#                 i += 1
#             final.append(inverse_in_parenthesis(temp)[::-1]) #we only reverse this part
#         else: # any other character, treat as normal
#             final.append(string[i])
#             i += 1
#     return "".join(final)


# test cases
string = ''
assert inverse_in_parenthesis(string) == ''

string = 'a'
assert inverse_in_parenthesis(string) == 'a'

string = 'ab'
assert inverse_in_parenthesis(string) == 'ab'

string = 'abc'
assert inverse_in_parenthesis(string) == 'abc'

string = 'a(bc)'
assert inverse_in_parenthesis(string) == 'acb'

string = 'a(b(cd))'
assert inverse_in_parenthesis(string) == 'acdb'

string = 'a(b(c)d)'
assert inverse_in_parenthesis(string) == 'adcb'

string = 'a(b(c(de)f))'
assert inverse_in_parenthesis(string) == 'acedfb'

string = '()'
assert inverse_in_parenthesis(string) == ''

string = '(a)'
assert inverse_in_parenthesis(string) == 'a'

string = '(ab)'
assert inverse_in_parenthesis(string) == 'ba'

string = '(b(c(de)f))'
assert inverse_in_parenthesis(string) == 'cedfb'

string = '(ab)c(de)'
assert inverse_in_parenthesis(string) == 'baced'

string = '(ab)c(d(ef)g)'
assert inverse_in_parenthesis(string) == 'bacgefd'

print(inverse_in_parenthesis(string)) == 'acedfb'
