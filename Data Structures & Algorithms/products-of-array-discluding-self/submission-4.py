class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        (prefixes,suffixes) = self.computePartials(nums)
        lastIndex = len(nums)-1
        res = [self.getProd(suffixes, prefixes, lastIndex, i) for i in range(0,len(nums))]
        return res 

    def getProd(self, s: List[int], p: List[int], lastIndex: int, i: int) -> int:
        if i == 0: 
            return s[1]
        elif i == lastIndex:
            return p[lastIndex-1]
        else:
            return p[i-1]*s[i+1]

    def computePartials(self, nums: List[int]) -> (List[int], List[int]):
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        lastIndex = len(nums)-1
        prefix[0] = nums[0]
        suffix[lastIndex] = nums[lastIndex]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
            suffix[lastIndex-i] = suffix[lastIndex-i+1]*nums[lastIndex-i]

        return (prefix,suffix)
        