class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # Time complexity: O(n)
        # Space complexity: O(n)
        for i in range(len(nums)):
            if nums[i] in seen: 
                return True 
            seen.add(nums[i])
        
        return False 