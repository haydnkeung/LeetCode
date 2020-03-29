class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        result = list()
        A.sort()
        for bitem in B:
            if A[len(A)-1] <= bitem:
                result.append(A[0])
                A.pop(0)
            else:
                aindex = self.binsearch(A,bitem,0,len(A)-1,0)
                while aindex != len(A):
                    if A[aindex] > bitem:
                        result.append(A[aindex])
                        A.pop(aindex)
                        break
                    aindex+=1             
        return result
    
    def binsearch(self, A:List[int],Bval:int, lo:int,hi:int,oldMid:int) -> int:
        if lo > hi:
            return oldMid
        mid = (lo + hi) // 2
        if A[mid] == Bval:
            return mid
        elif A[mid] < Bval:
            return self.binsearch(A,Bval,mid+1,hi,mid)
        elif A[mid] > Bval:
            return self.binsearch(A,Bval,lo,mid-1,mid)