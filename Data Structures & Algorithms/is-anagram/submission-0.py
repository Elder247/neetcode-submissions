class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1, cnt2 = {}, {}

        for char1 in s:
            cnt1[char1] = cnt1.get(char1, 0) + 1
        
        for char2 in t:
            cnt2[char2] = cnt2.get(char2, 0) + 1
        
        return cnt1 == cnt2