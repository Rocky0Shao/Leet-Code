class Solution:
    def climbStairs(self, n):
        if n <= 1: return 1
        init = [0,1]
        for i in range(0,n):
            init.append(init[-1] + init [-2])
        return init[-1]
