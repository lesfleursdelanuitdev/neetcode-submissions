class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for word in strs: 
            sortedWord = ''.join(sorted(word))
            if sortedWord not in grouped: 
                grouped[sortedWord] = []

            grouped[sortedWord].append(word)

        res = []
        for sortedWord in grouped: 
            res.append(grouped[sortedWord])

        return res
            