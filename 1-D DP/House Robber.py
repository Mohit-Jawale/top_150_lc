## dfs+memo

class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)-1
        memo = {}

        def dfs(n):

            if n<0:
                return 0

            if n in memo:
                return memo[n]    

            memo[n]= max(dfs(n-2)+nums[n],dfs(n-1))

            return memo[n]    


        return dfs(n)   




### 1-D

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]
