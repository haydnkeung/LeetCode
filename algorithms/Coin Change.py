class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = dict()
        x = self.compute(coins, amount)
        return x
    
    
    def compute(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        elif amount in self.memo:
            return self.memo[amount]
        
        record = 2 << 31
        for item in coins:
            temp = self.compute(coins, amount - item)
            if temp + 1 < record and temp >= 0:
                record = temp + 1    
        if record == 2 << 31:
            record = -1
            
        self.memo[amount] = record
        return record
                