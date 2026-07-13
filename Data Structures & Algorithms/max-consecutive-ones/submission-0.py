class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # I think we can use Kadane's Algorithm here. 
        globalMaxSpan = 0 # initialize the global max span to 0 
        localMaxSpan = 0 # initialize the local max span to 0 
        for i in range(0, len(nums)):
            #print(nums[i])
            localMaxSpan = localMaxSpan + 1 if nums[i] == 1 else 0
            globalMaxSpan = globalMaxSpan if globalMaxSpan > localMaxSpan else localMaxSpan

        return globalMaxSpan