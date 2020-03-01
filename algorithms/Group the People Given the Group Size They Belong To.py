class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        myMap = dict()
        result = list()
        for counter in range(len(groupSizes)):
            if groupSizes[counter] in myMap.keys():
                myMap[groupSizes[counter]].append(counter)
            else:
                myMap[groupSizes[counter]] = [counter]
        for key in myMap.keys():
            myList = myMap[key]
            myGroupSize = int(len(myList) / key)
            startIndex = 0
            while startIndex < len(myList):
                result.append(myList[startIndex:startIndex + key])
                startIndex += key
        return result