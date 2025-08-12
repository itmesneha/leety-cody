class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for word in strs:
            temp = sorted(word)
            sorted_word = ''.join(temp)
            # print(sorted_word)
            lst = di.get(sorted_word, [])
            lst.append(word)
            di[sorted_word] = lst
        return(list(di.values()))