"""
Description

Given a string S and a string T, find the minimum window in S which will contain all the characters
in T in complexity O(n).

Return the string that represents this minimum window that contains “ABC”
"""
import string


# My solution 1
def mininum_window(s, t):
    char_needed = charFreq(t)

    l, r = 0, 0
    window_length = float('inf')
    recent_ind = {c: [-1] * char_needed[ord(c)] for c in string.ascii_uppercase}

    while l < len(s):
        if char_needed[ord(s[r])] > 0:
            r += 1
            char_needed[ord(s[r])] -= 1
            recent_ind[ord(s[r])].pop(0)
            recent_ind[ord(s[r])].append(r)
            if not any(charFreq):
                window_length = min(window_length, r - l)
        elif l in recent_ind[ord(s[r])]:
            recent_ind[ord(s[r])].pop(0)
            recent_ind[ord(s[r])].append(r)
            l = recent_ind[ord(s[r])][0]
            if not any(charFreq):
                window_length = min(window_length, r - l)

    return window_length


def charFreq(t):
    char_freq = [0]*26
    for c in t:
        char_freq[ord(c)] += 1
    return char_freq

# Derrick's solution
# function minWindowSubstring(S, T) {
#   // [Initialization: See shortly after question description]
#   let slow = 0;
#   for(let fast = 0; fast < S.length; fast++) {
#     if(S[fast] in windowCounts) {
#       windowCounts[S[fast]] += 1
#       if(windowCounts[S[fast]] == requiredCounts[S[fast]]) {
#         missingCharacters -= 1;
#       }
#     }
#     // Shrink window until you have an incomplete set
#     while (missingCharacters === 0) {
#       // Updates result range if smaller than previous range
#       if((fast - slow) < (shortest[1] - shortest[0])) {
#         shortest[0] = slow
#         shortest[1] = fast
#       }
#       if(S[slow] in windowCounts) {
#         windowCounts[S[slow]] -= 1
#         if(windowCounts[S[slow]] < requiredCounts[S[slow]]) {
#           missingCharacters += 1
#         }
#       }
#       slow += 1;
#     }
#   }
#   return shortest[1] === Infinity ? "No Substring"
#                      : S.slice(shortest[0], shortest[1] + 1);
# }