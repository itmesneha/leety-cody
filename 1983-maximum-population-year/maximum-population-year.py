class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = []
        deaths = []
        for born, death in logs:
            births.append(born)
            deaths.append(death)

        births.sort()
        deaths.sort()

        max_population = 1
        cur = 1
        ans_year = births[0]
        i = 1
        j = 0
        
        n = len(logs)

        while i < n and j < n:
            if births[i] < deaths[j]: # another person was born before the last one died
                cur += 1
                if cur > max_population:
                    ans_year = births[i]
                    max_population = cur
                i += 1
            else:
                j += 1
                cur -= 1

        return ans_year