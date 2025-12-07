class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        if even number sum median = mean(((n1 + n2) // 2) - 1,(n1 + n2) // 2)
        if odd, median = floor((n1 + n2) // 2)
        
        2 pointers
        '''
        p1 = 0
        p2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        temp = []
        while p1 < n1 and p2 < n2:
            if nums1[p1] <= nums2[p2]:
                temp.append(nums1[p1])
                p1 += 1
                # print('p1: ', p1)
            
            elif nums1[p1] > nums2[p2]:
                temp.append(nums2[p2])
                p2 += 1
                # print('p2: ', p2)
                

        # print('temp: ', temp)
        if p1 < n1:
            for x in nums1[p1:]:
                temp.append(x)
           
        if p2 < n2:
             for x in nums2[p2:]:
                temp.append(x)

        # print('temp: ', temp)
        if (n1 + n2) % 2 == 0: # even
            second = total // 2
            first = second - 1
            median = (temp[first] + temp[second]) / 2
        
        else:
            median = temp[total // 2]

        return median