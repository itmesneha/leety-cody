class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = {}
       freq = [[] for i in range(len(nums)+1)]
       print('count:', count)
       print('freq:', freq)

       for n in nums:
          count[n] = 1 + count.get(n,0)

    #    print('count: ', count)  
    #    print('count.items() : ', count.items())

       for n,c in count.items():
            freq[c].append(n)
            # print('freq:', freq)
       output = []
    #    print('len freq:', len(freq)) 
       for i in range(len(freq) - 1, 0, -1):
        #    print('i:', i)
        #    print('freq[i]:', freq[i])
           for n in freq[i]: #Only goes into freq[i] if something is present inside
            output.append(n)
            # print('output: ', output)
            if len(output) == k:
               return output

