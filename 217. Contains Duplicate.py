class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)

        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if hashmap.get(n):
                return True
            else:
                hashmap[n] = hashmap.get(n,0) + 1
        return False

        
