class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs: 
            freqs = self.computeFrequencies(s)
            if freqs not in grouped: 
                grouped[freqs] = [s]
            else:
                grouped[freqs].append(s)

        res = []
        for freqs in grouped: 
            res.append(grouped[freqs])

        return res

    def computeFrequencies(self, word: str) -> str: 
        freqs = [0 for i in range(0,26)]
        for c in word: 
            pos = ord(c) - ord('a')
            freqs[pos] += 1

        return ','.join([str(f) for f in freqs])