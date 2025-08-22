class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hmap = Counter(hand)
        nums = sorted(hmap.keys())
        for num in nums:
            while hmap[num] > 0:
                for i in range(groupSize):
                    if hmap[num+i] <= 0:
                        return False
                    hmap[num + i] -= 1
        return True