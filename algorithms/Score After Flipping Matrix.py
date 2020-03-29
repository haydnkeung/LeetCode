class Solution:
    verticalToggle = "vertical"
    horizontalToggle = "horizontal"
    
    def toggleMatrix(self, orientation: str, index: int, A: List[List[int]]) -> List[List[int]]:
        if orientation == self.verticalToggle:
            bounds = len(A)
            for curPos in range(bounds):
                A[curPos][index] ^= 1
        else:
            bounds = len(A[0])
            for curPos in range(bounds):
                A[index][curPos] ^= 1
        return A
    
    def sumMatrix(self, A: List[List[int]]):
        total = 0
        for curRow in range(len(A)):
            partialSum = 0
            value = 1
            for curCol in range(len(A[0])):
                if A[curRow][len(A[0]) - curCol - 1] == 1:
                    # print("("+str(curRow)+","+str(len(A[0]) - curCol - 1)+"="+str(A[curRow][len(A[0]) - curCol - 1]))
                    partialSum += value
                value *= 2
                # print(value)
            total += partialSum
            #print(partialSum)        
        return total
                
    def getNumberOfOnes(self, curCol: int, A: List[List[int]]) -> int:
        result = 0
        for counter in range(len(A)):
            if A[counter][curCol] == 1:
                result += 1
        return result
    def matrixScore(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        for curCol in range(cols):
            numberOfOnes = self.getNumberOfOnes(curCol,A)
            A = self.toggleMatrix(self.verticalToggle,curCol,A)
            newNumberOfOnes = self.getNumberOfOnes(curCol,A)
            if newNumberOfOnes < numberOfOnes:
                self.toggleMatrix(self.verticalToggle,curCol,A)
            for curRow in range(rows):
                if A[curRow][curCol] == 0:
                    safe = True
                    for rowCheck in range(curCol):
                        if A[curRow][rowCheck] == 1:
                            safe = False
                            break
                    if safe:
                        self.toggleMatrix(self.horizontalToggle, curRow,A)
        # print(A)
        return self.sumMatrix(A)