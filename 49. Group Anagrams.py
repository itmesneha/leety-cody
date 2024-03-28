class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # res = dict([])
        # print('res:', res)
        for s in strs: #for every word in the list
            count = [0] * 26 #a.....z
            # print('count: ', count)

            for c in s: #for every character in the word
                count[ord(c) - ord('a')] += 1
            # print('count:', count)

            res[tuple(count)].append(s) 
            #The error "TypeError: unhashable type: 'list'" occurs when you try to use a    list object as a key in a dictionary or as an element in a set. Lists are mutable and therefore not hashable. Hashable objects are objects with a hash value that does not change over time. Examples of hashable objects include tuples and strings. To solve this error, you can ensure that you only assign a hashable object as a key for a dictionary. For example, you can convert a list to a tuple before using it as a key.
            # print('res:', res)

        return res.values()


    #   res = dict()
    #   print(res)
