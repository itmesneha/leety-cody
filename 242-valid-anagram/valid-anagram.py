class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one way to use hashmap
        # sorting
        # sets ??
        # set(s) = (a,n,g,r,m)
        # set(t) = (n,a,g,r,m)
        # print(set(s))
        # print(set(t))
        # return set(s) == set(t) # count matters
        hash_s = Counter(s)
        hash_t = Counter(t)
        # print(hash_s)
        # print(hash_t)
        return hash_s == hash_t
        
