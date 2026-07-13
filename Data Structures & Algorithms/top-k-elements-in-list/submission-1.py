import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums: 
            if n not in freqs: 
                freqs[n] = 0 

            freqs[n] += 1 

        pq = []
        for n in freqs: 
            heapq.heappush(pq, (-freqs[n], n))

        res = []
        for i in range(0, k):
            res.append(heapq.heappop(pq)[1])

        return res


