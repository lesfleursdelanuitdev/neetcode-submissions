class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        (prefixes,suffixes) = self.computePartials(nums)

        def getProd(i, lastIndex):
            if i == 0: 
                return suffixes[1]
            elif i == lastIndex: 
                return prefixes[lastIndex-1]
            else:
                return prefixes[i-1]*suffixes[i+1]

        res = [getProd(i, len(nums)-1) for i in range(0,len(nums))]
        return res 

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
        