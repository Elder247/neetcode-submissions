class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += "ы" + s
        return result

    def decode(self, s: str) -> List[str]:
        return s.split("ы")[1:]
