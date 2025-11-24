class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in map the keys will be maps but maps, lists are unhashable
        # [e:1, a:1, t:1] : [eat,tea,ate]
        main_map = defaultdict(list)
        for word in strs:
            # print(''.join(sorted(word)))
            main_map[''.join(sorted(word))].append(word)

        # print(values(main_map))
        return list(main_map.values())