class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonZeroProd = 1
        prod = 1
        seenZero = False
        for n in nums: 
            prod = prod * n 
            if not seenZero: 
                if n == 0: 
                    seenZero = True
                else: 
                    nonZeroProd = nonZeroProd * n
            else: 
                nonZeroProd = nonZeroProd * n

        res = []
        for i in range(len(nums)):
            if not nums[i] == 0: 
                res.append(int(prod/nums[i]))
            else: 
                res.append(nonZeroProd)
        return res