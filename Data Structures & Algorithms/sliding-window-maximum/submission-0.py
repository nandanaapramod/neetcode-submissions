class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]

        for i in range(len(nums)-k+1):
            large=nums[i]
            for j in range(i,i+k):
                
                    large=max(large,nums[j])
                    
            res.append(large)
        return res