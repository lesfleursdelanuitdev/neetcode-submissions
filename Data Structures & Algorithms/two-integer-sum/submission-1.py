class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # determine what number you need to reach target for each 
        # element in array 
        if len(nums) == 2: 
            return [0,1] # this must be the answer if the length is two 

        
        seenList = {} # The keys of this dictionary are the values in nums and the values are a list of indexes where one can find that value in nums 
        for i in range(len(nums)):
            if nums[i] not in seenList: 
                seenList[nums[i]] = [i]
            else:
                seenList[nums[i]].append(i)

        print(seenList)

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seenList: 
                # case #1 
                if difference == nums[i]:
                    if len(seenList[difference]) == 2: 
                        return seenList[difference]
                else:
                    if i < seenList[difference][0]:
                        return [i, seenList[difference][0]]
                    else: 
                        return [seenList[difference][0],i]