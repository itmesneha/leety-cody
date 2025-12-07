class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        if even number sum median = mean(((n1 + n2) // 2) - 1,(n1 + n2) // 2)
        if odd, median = floor((n1 + n2) // 2)
        
        then 2 pointers
        '''
        p1 = 0
        p2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        counter = 0
        if total % 2 == 0:
            index_second = total // 2
            index_first = index_second - 1

        else:
            index_second = total // 2
            index_first = total // 2
        
        while p1 < n1 and p2 < n2:
            if nums1[p1] <= nums2[p2]:
                if counter == index_second:
                    second_element = nums1[p1]
                if counter == index_first:
                    first_element = nums1[p1]
                p1 += 1

            else:
                if counter == index_second:
                    second_element = nums2[p2]
                if counter == index_first:
                    first_element = nums2[p2]

                p2 += 1

            counter += 1

        while p1 < n1:
            if counter == index_first:
                first_element = nums1[p1]

            if counter == index_second:
                second_element = nums1[p1]
                break
            p1 += 1

            counter += 1
           
        while p2 < n2:
            if counter == index_first:
                first_element = nums2[p2]

            if counter == index_second:
                second_element = nums2[p2]
                break
            p2 += 1

            counter += 1

        if index_first == index_second:
            return  first_element
        return (first_element + second_element) / 2

      