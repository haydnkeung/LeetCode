class Solution:
    def compute(self, val: int, myList: List[int]) -> List[int]:
        if val == 1:
            return myList
        level = int(math.log(val, 2))
        temp = (((2 ** (level + 1)) - 1) - val) // 2
        newVal = 2 ** (level - 1) + temp
        return self.compute(newVal, [newVal] + myList)
    
    def pathInZigZagTree(self, label: int) -> List[int]:
        return self.compute(label, [label])
    