class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        items = sorted(counter.items(), key=lambda item: item[1])[-k:]
        return list(map(lambda item: item[0], items))