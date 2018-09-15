
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(0,len(A)):
            if A[i]>A[i+1]:
                return i

