"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        
        def traverseToList(root: 'Node', myList) -> List['Node']:
            if root == None:
                return myList
            myList = traverseToList(root.left, myList)
            myList.append(root)
            myList = traverseToList(root.right, myList)
            return myList
        
        myList = traverseToList(root, [])
        counter = 1
        for i, item in enumerate(myList):
            if item.next == None:
                counter *= 2
                for j in range(i, len(myList), counter):
                    if j + counter <= len(myList) - 1:
                        myList[j].next = myList[j + counter]
        return root