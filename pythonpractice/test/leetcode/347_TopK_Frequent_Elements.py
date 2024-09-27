class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)

        for e in nums:
            freq[e] += 1
        
        pq = [] # 기본으로 min heap (오름차순)
        for value, frequency in freq.items():
            heapq.heappush(pq, (-frequency, value))

        res = []
        while k > 0:
            k -= 1
            res.append(heappop(pq)[1])
        return res
