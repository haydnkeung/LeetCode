from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        prev = 0
        cur = nums[0]
        while prev <= cur:
            if cur >= len(nums) - 1:
                break
            temp = prev + nums[prev]
            if temp > cur:
                cur = temp
            prev += 1
            
        return cur >= len(nums) - 1
        