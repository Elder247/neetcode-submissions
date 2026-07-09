class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        pref[0] = nums[0]

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i]
        
        suf = [0] * len(nums)
        suf[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = suf[i + 1]
            elif i == len(nums) - 1:
                result[i] = pref[i - 1]
            else:
                result[i] = pref[i - 1] * suf[i + 1]
        
        return result