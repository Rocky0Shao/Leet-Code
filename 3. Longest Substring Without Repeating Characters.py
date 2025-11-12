class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_word = ""
        for pointer in range(0,len(s)):
            current = "" 
            for char in s[pointer:]:
                if char not in current:
                    current += char
                else:
                    break
            if len(current) > len(longest_word):
                longest_word = current
        return len(longest_word)
