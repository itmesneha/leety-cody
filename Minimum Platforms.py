class Solution:    
    def minPlatform(self, arr, dep):
        n = len(arr)  
        
        platforms = 1 # at least 1 platform you will need
        ans = 1
        
        i = 1 # next arrival
        j = 0 # first departure
        
        arr.sort()
        dep.sort()
        
        while i < n and j < n:
            if dep[j] < arr[i]:
                platforms -= 1 # coz train went
                j += 1
                
            else: # before anything is leaving how many trains are coming in
                platforms += 1
                i += 1
                ans = max(ans, platforms)
                
        return ans

        # li = []
        # for i in range(n):
        #     li.append((arr[i], 1))
        #     li.append((dep[i], -1))
            
        # li.sort(key = lambda x : (x[0], -x[1]))
        
        # cur = 0
        # ans = 0
        # for event in li:
        #     cur = cur + event[1]
        #     ans = max(ans, cur)

        # return ans            
        
        
