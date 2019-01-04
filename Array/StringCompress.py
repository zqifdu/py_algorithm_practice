# Cracking the Coding interview: 1.6

import re


def string_compression(string):
    # Empty string
    if not string:
        return ''

    len_origin = len(string)
    original_string = string

    last_ch = '!'
    i = 0
    insert_len = 0
    while True:
        if i >= len(string):
            break
        # if current character is the same as last one
        if string[i] == last_ch:
            # update the counting
            count += 1
            # take away the current character
            string = string[:i] + string[i+1:]
        else:
            if i > 0:
                insert_len = len(str(count))
                string = string[:i] + str(count) + string[i:]
            # reset the count
            count = 1
            # update last_ch
            last_ch = string[i+insert_len]
            # Move forward; 2 because we've inserted a digit
            i += (1+insert_len)

    string += str(count)
    if len(string) > len_origin:
        return original_string
    return string


# test cases:
# test empty string
s = ''
assert string_compression(s) == ''

# test string that has longer 'compressed' string
s = 'a'
assert string_compression(s) == 'a'
s = 'ab'
assert string_compression(s) == 'ab'
s = 'abcccd'
assert string_compression(s) == 'abcccd'

# test string that has shorter compressed string
s = 'aaaabccc'
assert string_compression(s) == 'a4b1c3'

# test string that has more than 9 repetitions for a character
s = 'aaaaaaaaaab'
assert string_compression(s) == 'a10b1'



