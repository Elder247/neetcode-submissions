class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # req_number: position

        for ind, numb in enumerate(nums):
            if numb in hash_map:
                return [hash_map[numb], ind]

            req_number = target - numb
            hash_map[req_number] = ind