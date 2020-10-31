from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        q = PriorityQueue()
        for my_list in lists:
            cur = my_list
            while cur != None:
                q.put(cur.val)
                print(cur.val)
                cur = cur.next
                
        if q.empty():
            return None

        start = ListNode()
        start.val = q.get()
        prev = start
        cur = start
        while q.empty() == False:
            cur = ListNode()
            cur.val = q.get()
            prev.next = cur
            prev = cur
        
          
        return start