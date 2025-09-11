from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if sorted(word1) == sorted(word2):
            return True

        if len(word1) != len(word2):
            return False
            
        map1 = Counter(word1)
        map2 = Counter(word2)

        if sorted(map1.keys()) == sorted(map2.keys()) and sorted(map1.values()) == sorted(map2.values()):
            return True
        
        
        return False