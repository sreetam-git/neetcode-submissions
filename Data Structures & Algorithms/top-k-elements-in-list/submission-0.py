class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        output = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = dict(sorted(freq.items(), key= lambda x: x[1], reverse=True))
        
        for i, key in enumerate(sorted_freq.keys()):
            if i < k:
                output.append(key)

        return output 