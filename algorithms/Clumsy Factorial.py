class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        myList = list()
        operator = 0
        term = 0
        for i in range(N, 0, -1):
            if operator == 0:
                term = i
            elif operator == 1:
                term *= i
            elif operator == 2:
                term = term // i
                myList.append(term)
            elif operator == 3:
                myList.append(i)
        
            if i == 1 and operator != 2 and operator != 3:
                myList.append(term)
            
            operator += 1
            operator %= 4
            
        sum = myList[0]
        for i in range(1, len(myList)):
            if i % 2 == 1:
                sum += myList[i]
            else:
                sum -= myList[i]
        return sum
                
            
        