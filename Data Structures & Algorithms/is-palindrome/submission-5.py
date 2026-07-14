class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1 
        while l < r: 
            # are both chars valid? 
            while l < len(s) and not self.isAlphanumeric(s[l].lower()): 
                l += 1 
            while r >= 0 and not self.isAlphanumeric(s[r].lower()):
                r -= 1 
            
            # if you get here, both chars should be alphanumeric 
            if l < len(s) and r >= 0 and not s[l].lower() == s[r].lower():
                return False

            l += 1 
            r -= 1

        return True

    def isAlphanumeric(self, c):
        return "0" <= c <= "9" or "a" <= c <= "z"