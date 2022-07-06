class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leftpointer = 0
        total = 0
        res = float("inf")
        
        for rightpointer in range(len(nums)):
            total += nums[rightpointer]
            while total >= target:
                res = min(rightpointer - leftpointer + 1, res)
                total -= nums[leftpointer]
                leftpointer += 1
                
        return 0 if res == float("inf") else res
            