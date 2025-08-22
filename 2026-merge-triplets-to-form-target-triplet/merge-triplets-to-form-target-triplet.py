class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good_indices = set()
        for tri in triplets:
            if len(good_indices) == 3:
                return True
            temp = []
            valid = True
            for i in range(3):
                if tri[i] > target[i]:
                    # bad triplet 
                    valid = False
                    break
                if tri[i] == target[i]:
                    temp.append(i)
            if valid:
                for x in temp:
                    good_indices.add(x)
            # print('good_indices: ', good_indices, 'tri: ', tri)
        # print('good_indices: ', good_indices)
        if len(good_indices) == 3:
                return True
        else:
            return False
        