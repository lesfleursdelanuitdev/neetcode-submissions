class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        (prefixes,suffixes) = self.computePartials(nums)
        n = len(nums)
        lastIndex = n-1
        res = [self.getProd(suffixes, prefixes, lastIndex, i) for i in range(n)]
        return res 

    def getProd(self, s: List[int], p: List[int], lastIndex: int, i: int) -> int:
        if i == 0: 
            return s[1]
        elif i == lastIndex:
            return p[lastIndex-1]
        else:
            return p[i-1]*s[i+1]

    def computePartials(self, nums: List[int]) -> (List[int], List[int]):
        n = len(nums)
        p = [1]*n
        s = [1]*n
        lastIndex = n-1
        p[0] = nums[0]
        s[lastIndex] = nums[lastIndex]

        for i in range(1,n):
            p[i] = p[i-1]*nums[i]
            s[lastIndex-i] = s[lastIndex-i+1]*nums[lastIndex-i]

        return (p,s)
        