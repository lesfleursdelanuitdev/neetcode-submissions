class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Let A be an array with n elements. Let i be any 
        # particular element in the array. Then, define
        # prefix(A,i) as A[0]*A[1]*...*A[i]
        # 
        # We can also state this recursively as: 
        # prefix(A,i) = prefix(A,i-1)*A[i] 
        #prefixes = self.computePrefixes(nums)

        # Now define suffix(A,i) = A[n-i]*A[n-i-1]*...*A[1]*A[0]
        #suffixes = self.computeSuffixes(nums)
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

    def computePrefixes(self, nums: List[int]) -> List[int]:
        # initialize prefix[0] = nums[0]
        prefix = [1 for i in range(len(nums))]
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]

        return prefix 

    def computeSuffixes(self, nums: List[int]) -> List[int]:
        suffix = [1 for i in range(len(nums))]
        lastIndex = len(nums)-1
        suffix[lastIndex] = nums[lastIndex]

        for i in range(1,len(nums)):
            suffix[lastIndex-i] = suffix[lastIndex-i+1]*nums[lastIndex-i]

        return suffix
        