class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            sorted_s = "".join(sorted(s))  # Sort the characters of the string
            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]

        return list(anagram_map.values())
