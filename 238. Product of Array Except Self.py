class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        # print(output)

        #taking prefixes
        prefix = 1
        for i in range(len(nums) -1 ):
            prefix *= nums[i]
            output[i + 1] *= prefix
        # print('prefix output: ', output)  
        
        #taking postfixes
        postfix = 1
        for i in range(len(nums) - 1, 0 , -1):
            postfix *= nums[i]
            output[i - 1] *= postfix
        # print('postfix output: ', output)   

        return output

        # output = [1] * (len(nums))
        # # print('output: ', output)
        # for i in range(len(nums)):
        #     for j in range(len(output)):
        #         if i == j:
        #             continue
        #         output[j] = output[j] * nums[i]
        #         # print('output: ', output)
        # return output
            
