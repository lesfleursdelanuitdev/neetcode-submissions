class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        # determine the character distribution for each string 
        charDist = {}
        charDist["s"] = self.determineCharDistribution(s)
        charDist["t"] = self.determineCharDistribution(t)

        if not len(charDist["s"].keys()) == len(charDist["t"].keys()):
            return False 

        for k in charDist["s"].keys():
            if k not in charDist["t"].keys():
                return False

            if not charDist["t"][k] == charDist["s"][k]:
                return False

        return True  

    def determineCharDistribution(self, s: str) -> dict: 
        seen = {}
        for c in s: 
            if c not in seen: 
                seen[c] = 0 

            seen[c] += 1

        return seen 