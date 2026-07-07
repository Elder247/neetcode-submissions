class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for word in strs:
            counter = [0] * (ord('z') - ord('a') + 1)
            for char in word:
                position = ord(char) - ord('a')
                counter[position] += 1
            
            tuple_counter = tuple(counter)
            hash_table.setdefault(tuple_counter, []).append(word)
        
        return [value for value in hash_table.values()]