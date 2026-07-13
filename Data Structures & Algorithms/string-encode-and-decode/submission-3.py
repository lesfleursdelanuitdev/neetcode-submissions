class Solution:
    def encode(self, strs: List[str]) -> str:
        # for each string, we have the following format: 
        # #len#word
        encoded = []
        for s in strs: 
            curr = "#" + str(len(s)) + "#" + s 
            encoded.append(curr)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            if s[i] == "#":
                (wordLen, i) = self.getLength(s,i)
                startIndex = i + 1 
                endIndex = i + 1 + wordLen
                words.append(s[startIndex:endIndex])
                i = endIndex
            
        return words

    def getLength(self, s: str, i: int) -> (int, int):
        i += 1 # move past the hashtag
        num = ''
        while i < len(s) and not s[i] == "#":
            num += s[i]
            i += 1

        return (int(num), i)
 