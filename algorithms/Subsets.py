class Solution:
    
    def recurse(self, num: List[int]) -> List[List[int]]:
        if len(num) == 1:
            return [num]
        result = []
        result.append([num[0]])
        mysubsets = self.recurse(num[1:])
        for item in mysubsets:
            result.append(item)
            temp = [num[0]] + item
            result.append(temp)
        return result
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        result = self.recurse(nums)
        result.append([])
        return result