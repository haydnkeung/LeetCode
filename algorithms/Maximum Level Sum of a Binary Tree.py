# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getResult(self) -> int:
        myKeys = list(self.myDict.keys())
        highest = self.myDict[myKeys[0]]
        result = myKeys[0]
        for index in range(len(myKeys)):
            curKey = myKeys[index]
            if self.myDict[curKey] > highest:
                highest = self.myDict[curKey]
                result = curKey
        return result
    def add(self, depth: int, root: TreeNode):
        #print("My val is "+str(root.val))
        if root.left != None:
            self.add(depth + 1, root.left)
        if root.right != None:
            self.add(depth + 1, root.right)
        if depth in self.myDict.keys():
            newValue = self.myDict[depth] + root.val
            self.myDict[depth] = newValue
            #print("Adding "+str(root.val)+" to depth of "+str(depth))
            #print("new value is "+str(self.myDict[depth]))
        else:
            self.myDict[depth] = root.val
            #print("*Adding "+str(root.val)+" to depth of "+str(depth))
            #print("new value is "+str(self.myDict[depth]))
         
    def maxLevelSum(self, root: TreeNode) -> int:
        self.myDict = {}
        self.add(1, root)
        #print(str(self.myDict))
        return self.getResult()