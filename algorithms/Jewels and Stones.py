class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set()
        result = 0
        for x in J:
            jewels.add(x)
        for y in S:
            if y in jewels:
                result = result + 1
        return result
        