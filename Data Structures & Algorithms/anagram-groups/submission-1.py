class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs: 
            anagramFound = False 
            for group in groups.keys():
                if self.isAnagram(group,word):
                    anagramFound = True 
                    print(group + " is an anagram of " + word)
                    groups[group].append(word)
                    print(groups[group])
                    break
            
            if not anagramFound: 
                groups[word] = [word]
                
        res = []
        for group in groups: 
            res.append(groups[group])

        print(res)
        return res

    def isAnagram(self, w1: str, w2: str) -> bool: 
        if not len(w1) == len(w2):
            return False 

        counts1 = self.doCounts(w1)
        counts2 = self.doCounts(w2)

        return self.compareFrequencies(counts1,counts2)
    
    def doCounts(self, w: str) -> dict: 
        counts = {}
        for i in range(len(w)):
            if w[i] not in counts: 
                counts[w[i]] = 0 

            counts[w[i]] += 1 
        return counts 

    def compareFrequencies(self, c1: dict, c2: dict) -> bool: 
        if not len(c1.keys()) == len(c2.keys()):
            return False

        for k in c1:
            if k not in c2: 
                return False

            if not c1[k] == c2[k]:
                return False 

        return True