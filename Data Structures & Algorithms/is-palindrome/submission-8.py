class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1 
        s = [c for c in s.lower()]
        while l < r: 
            # are both chars valid? 
            l = self.getLeftIndex(s,l)
            r = self.getRightIndex(s,r)
            # if you get here, both chars should be alphanumeric 
            if l < len(s) and r >= 0 and not s[l] == s[r]:
                return False

            l += 1 
            r -= 1

        return True

    def getLeftIndex(self, s, left):
        # keep moving forward until you find an alphanumeric character 
        # or reach the end of the string. Once either condition is met, 
        # return the value of left
        while left < len(s) and not self.isAlphanumeric(s[left]):
            left += 1
        return left 

    def getRightIndex(self,s, right):
        # Keep moving backwards until you find an alphanumeric character 
        # or reach the beginning of the string. Once either condition is met, 
        # return right 
        while right >= 0 and not self.isAlphanumeric(s[right]):
            right -= 1 

        return right

    def isAlphanumeric(self, c):
        return "0" <= c <= "9" or "a" <= c <= "z"