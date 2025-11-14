

'''
Brute Force Solution
Time Limit Exceeded
'''
def isPalindrome(s):

    for i in range(int(len(s)/2)):
        l_str = s[i]
        r_str = s[len(s) -1 -i]
        if l_str != r_str: return False
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for l in range(0,len(s)):
            
            for r in range(l,len(s)):
                current_word = s[l : r+1]
                if isPalindrome(current_word) and len(current_word) > len(out):
                    out = current_word
        return out
'''
Mid-Expand Paliindrome Search
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(l, r):
            # Expand around center (l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Return the palindrome slice
            return s[l+1:r]

        longest = ""

        for i in range(len(s)):
            # Odd-length apalindrome
            p1 = expand(i, i)
            # Even-length palindrome
            p2 = expand(i, i+1)

            # Update longest
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest

