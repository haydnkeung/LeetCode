# @Author: Haydn K
class MyHashMap:
# We need to active state to let the get function know that
# we may of placed items after that position. Without the active state
# the get would stop at the removed item and would no longer be able to access
# the item placed after the remove in amortized constant time
    
    capacity = 10001
    def __init__(self):
        self.list = [None] * self.capacity
        
        """
        Initialize your data structure here.
        """      
    def hash(self, key: int) -> int:
        return ((key << 32) + key) % self.capacity

    def put(self, key: int, value: int) -> None:
        pos = self.hash(key)
        
        while None != self.list[pos] and self.list[pos][0] != key:
            pos = pos + 1
            if pos == self.capacity:
                pos = 0
#                 The boolean specifies whether the item is active
        self.list[pos] = (key, value, True)
        
        """
        value will always be non-negative.
        """
        
    def get(self, key: int) -> int:
        pos = self.hash(key)
        count = 0
        
        while None != self.list[pos] and self.list[pos][0] != key:
            pos = pos + 1
            count = count + 1
            if pos == self.capacity:
                pos = 0
            if count >= self.capacity:
                return -1
        if self.list[pos] == None:
            return -1
        elif self.list[pos][2] == True:
            return self.list[pos][1]
        else:
            return -1
        
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        count = 0
            
        while None != self.list[pos] and self.list[pos][0] != key:
            pos = pos + 1
            count = count + 1
            if pos == self.capacity:
                pos = 0
            if count >= self.capacity:
                return
        if None != self.list[pos]:
            self.list[pos] = (key,0,False)
                
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)