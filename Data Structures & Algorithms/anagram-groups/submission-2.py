class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []
        for word in strs: 
            anagramFound = False 
            for anagram in anagrams: 
                if self.isAnagram(word, anagram):
                    anagramFound = True 
                    res[anagrams[anagram]].append(word)

            if not anagramFound: 
                res.append([word])
                anagrams[word] = len(res) - 1
                

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