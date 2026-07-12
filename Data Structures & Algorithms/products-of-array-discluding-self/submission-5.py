class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out= [0] * n
       
        for i in range(n):
            product=1
            for j in range(n):
                if i==j:
                    continue
                product*=nums[j]
            out[i]=product
        return out