class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            if num % 3 != 0:
                out +=1
        return out
