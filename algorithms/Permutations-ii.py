class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def countItems(nums: List[int]):
            counterDict = dict()
            for num in nums:
                if num not in counterDict.keys():
                    counterDict[num] = 1
                else:
                    counterDict[num] += 1
            return counterDict
        
        def compute(counterDict):
            newCounter = dict()
            for key, val in counterDict.items():
                if val != 0:
                    newCounter[key] = val
            
            if len(newCounter) == 0:
                return [[]]
            result = []
            for key in newCounter.keys():
                newCounter[key] -= 1
                recurse = compute(newCounter)
                newCounter[key] += 1
                for subset in recurse:
                    newItem = [key] + subset
                    result.append(newItem)
            return result
                       
        return compute(countItems(nums))
        
                
        
        
        