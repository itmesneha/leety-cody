class TimeMap:
    '''
    binary search + hashmap.
    '''
    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([timestamp, value])
        # print(self.hmap)
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap[key]
        if not arr:
            return ''
        left = 0
        n = len(arr)
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return arr[right][1] if right >= 0 else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)