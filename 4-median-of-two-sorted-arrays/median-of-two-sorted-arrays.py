class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        if even number sum median = mean(((n1 + n2) // 2) - 1,(n1 + n2) // 2)
        if odd, median = floor((n1 + n2) // 2)
        
        then 2 pointers and build temp array. 
        or without temp array keep track of counter if counter = first or second index write logic.
        '''
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        if total == 0:                           
            return 0.0

        index_second = total // 2
        index_first = index_second if total % 2 else index_second - 1

        p1 = p2 = counter = 0
        first = second = 0

        # single merged loop — stop as soon as we have assigned second
        while counter <= index_second:
            if p1 < n1 and (p2 >= n2 or nums1[p1] <= nums2[p2]):
                val = nums1[p1]
                p1 += 1
            else:
                val = nums2[p2]
                p2 += 1

            if counter == index_first:
                first = val
            if counter == index_second:
                second = val

            counter += 1

        # if indices are same (odd total) return that element as float
        if index_first == index_second:
            return float(second)
        return (first + second) / 2.0

      