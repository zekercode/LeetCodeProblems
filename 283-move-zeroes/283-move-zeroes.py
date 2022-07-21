class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #both pointers starting at 0
        #let the right pointer traverse through the array
        #checking if each value is != 0
        #if it's not a zero let it switch places with left
        #incement the left by one after the switch
        #then increment the right pointer until the end
        
        left = 0
        right = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums